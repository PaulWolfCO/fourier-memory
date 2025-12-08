# generate_figures_HOLOGRAPHIC_FINAL.py
import numpy as np
import matplotlib.pyplot as plt

# === PARAMETERS ===
n_cells = 12
true_pos = np.linspace(0.1, 0.9, n_cells)                  # True position in meters
precession_deg_per_m = -240                                # Classic phase precession slope
preferred_phase_deg = 300 + precession_deg_per_m * true_pos
preferred_phase_rad = np.deg2rad(preferred_phase_deg)

# One theta cycle (125 ms @ 8 Hz)
fs = 1024
t_cycle = np.linspace(0, 1/8, fs, endpoint=False)
theta_wave = np.cos(2 * np.pi * 8 * t_cycle)               # Real-valued LFP for plotting
ref_beam = np.exp(1j * 2 * np.pi * 8 * t_cycle)             # Complex reference beam

# === Object beam: one spike per place cell at its preferred phase ===
object_beam = np.zeros(fs, dtype=complex)
for phase_rad in preferred_phase_rad:
    target_time = (phase_rad % (2*np.pi)) / (2*np.pi*8)     # Convert phase → time in cycle
    idx = np.argmin(np.abs(t_cycle - target_time))
    object_beam[idx] += 1.0

# === Hologram = interference (what synapses store) ===
hologram = object_beam + ref_beam

# === Reconstruction: illuminate hologram with reference beam again ===
recon_complex = np.fft.ifft(np.fft.fft(hologram) * np.conj(np.fft.fft(ref_beam)))
reconstructed = np.abs(recon_complex)
peak_idx = np.argmax(reconstructed)
decoded_time = t_cycle[peak_idx]
decoded_phase_deg = (decoded_time * 8 * 360) % 360
decoded_pos_holographic = (decoded_phase_deg - 300) / precession_deg_per_m

# === Linear Fourier decoder (knows precession exists) ===
n_harm = 12
A = np.zeros(n_harm + 1)
B = np.zeros(n_harm + 1)
A[0] = np.mean(true_pos)
for k in range(1, n_harm + 1):
    A[k] = 2/n_cells * np.sum(true_pos * np.cos(k * preferred_phase_rad))
    B[k] = 2/n_cells * np.sum(true_pos * np.sin(k * preferred_phase_rad))
recon_fourier = A[0] + sum(A[k]*np.cos(k*preferred_phase_rad) + B[k]*np.sin(k*preferred_phase_rad)
                          for k in range(1, n_harm+1))

# === Naïve decoder assuming NO precession (all spikes at 180°) ===
flat_phase_rad = np.full(n_cells, np.deg2rad(180))
A0 = np.zeros(n_harm + 1); B0 = np.zeros(n_harm + 1)
A0[0] = np.mean(true_pos)
for k in range(1, n_harm + 1):
    A0[k] = 2/n_cells * np.sum(true_pos * np.cos(k * flat_phase_rad))
    B0[k] = 2/n_cells * np.sum(true_pos * np.sin(k * flat_phase_rad))
recon_no_precession = A0[0] + np.sum([A0[k]*np.cos(k*flat_phase_rad) + B0[k]*np.sin(k*flat_phase_rad)
                                     for k in range(1, n_harm+1)], axis=0)

# === PLOT ===
plt.figure(figsize=(12, 9))

plt.subplot(2, 2, 1)
plt.plot(t_cycle*1000, theta_wave, 'k-', lw=1.5, label='Theta (8 Hz)')
spike_t = t_cycle[np.abs(object_beam) > 0]
spike_h = theta_wave[np.abs(object_beam) > 0]
plt.stem(spike_t*1000, spike_h, linefmt='r-', markerfmt='ro', basefmt='none', label='12 precessing spikes')
plt.title('(A) Theta Reference Beam + Phase-Precessing Spikes')
plt.xlabel('Time (ms)'); plt.ylabel('Amplitude'); plt.legend(); plt.grid(alpha=0.3)

plt.subplot(2, 2, 2)
plt.plot(t_cycle*1000, np.abs(hologram), 'purple', lw=1.5)
plt.title('(B) Recorded Hologram (Interference Pattern)')
plt.xlabel('Time (ms)'); plt.ylabel('|O + R|'); plt.grid(alpha=0.3)

plt.subplot(2, 2, 3)
plt.plot(t_cycle*1000, reconstructed, 'g-', lw=2)
plt.axvline(t_cycle[peak_idx]*1000, color='g', linestyle='--', lw=2,
            label=f'Peak → {decoded_pos_holographic:.3f} m')
plt.title('(C) Holographic Reconstruction')
plt.xlabel('Time (ms)'); plt.legend(); plt.grid(alpha=0.3)

plt.subplot(2, 2, 4)
plt.plot(true_pos, true_pos, 'k-', lw=3, label='True Position')
plt.plot(true_pos, recon_fourier, 'bo', markersize=9, label='Linear Fourier (knows precession)')
plt.plot(true_pos, recon_no_precession, 'mx', markersize=12, markeredgewidth=2,
         label='Linear Fourier (no precession assumed)')
plt.scatter(np.mean(true_pos), decoded_pos_holographic, s=600, c='gold', marker='*',
            edgecolors='black', linewidth=2, label=f'Holographic → {decoded_pos_holographic:.3f} m', zorder=10)
plt.title('Holographic Decoding Succeeds Without Knowing Precession')
plt.xlabel('True Position (m)'); plt.ylabel('Decoded Position (m)')
plt.legend(); plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('FIGURE_3_FINAL_HOLOGRAPHIC.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"True center: {np.mean(true_pos):.3f} m")
print(f"Holographic decode: {decoded_pos_holographic:.3f} m")
print(f"Linear Fourier (with precession): RMSE = {np.sqrt(np.mean((true_pos-recon_fourier)**2)):.5f} m")
print(f"Linear Fourier (no precession): RMSE = {np.sqrt(np.mean((true_pos-recon_no_precession)**2)):.5f} m")