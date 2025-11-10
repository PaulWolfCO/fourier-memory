# generate_figures.py
# Run this once → creates phase_precession.png + reconstruction.png
# Requires: pip install numpy matplotlib

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.figsize': (6.5, 4.0),
    'lines.linewidth': 1.5,
    'axes.linewidth': 0.8,
    'grid.linewidth': 0.5,
    'grid.alpha': 0.5
})

# ========================================
# FIGURE 1: Phase Precession (Raster + LFP)
# ========================================
np.random.seed(42)
n_cells = 12
track_length = 1.0  # meters
speed = 0.3  # m/s
theta_freq = 8  # Hz
T_theta = 1 / theta_freq
t_total = track_length / speed
t = np.linspace(0, t_total, 1000)

# Theta oscillation
theta = np.sin(2 * np.pi * theta_freq * t)

# Place fields (Gaussian centers)
centers = np.linspace(0.1, 0.9, n_cells)
width = 0.15
firing_rate = np.zeros((n_cells, len(t)))
for i, c in enumerate(centers):
    firing_rate[i] = 20 * np.exp(-((t * speed - c)**2) / (2 * width**2))

# Spikes (Poisson)
spikes = np.random.random(firing_rate.shape) < firing_rate * (t[1] - t[0])

# Phase precession: phase = 360° × (position / track_length)
position = speed * t
phase = 360 * (position / track_length) % 360

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6.5, 6), gridspec_kw={'height_ratios': [1, 1, 1]})

# (A) Raster
for i in range(n_cells):
    spike_times = t[spikes[i]]
    ax1.vlines(spike_times, i, i + 0.8, color='black', linewidth=0.8)
ax1.set_yticks(np.arange(n_cells) + 0.4)
ax1.set_yticklabels([f'Cell {i+1}' for i in range(n_cells)])
ax1.set_xlim(0, t_total)
ax1.set_ylabel('Place Cells')
ax1.set_title('(A) Place Cell Raster')

# (B) LFP + Spikes
ax2.plot(t, theta, 'k-', label='Theta (8 Hz)')
for i in range(n_cells):
    spike_times = t[spikes[i]]
    ax2.scatter(spike_times, [i*0.3]*len(spike_times), c='red', s=8, zorder=5)
ax2.set_xlim(0, t_total)
ax2.set_ylim(-1.2, 1.2)
ax2.set_ylabel('LFP / Spikes')
ax2.set_title('(B) Theta Oscillation with Spikes')
ax2.legend(loc='upper right')

# (C) Phase vs. Position
for i in range(n_cells):
    spike_pos = speed * t[spikes[i]]
    spike_phase = phase[spikes[i]]
    ax3.scatter(spike_pos, spike_phase, c=f'C{i}', s=12, alpha=0.7)
ax3.set_xlim(0, 1.0)
ax3.set_ylim(0, 360)
ax3.set_xlabel('Position (m)')
ax3.set_ylabel('Theta Phase (°)')
ax3.set_title('(C) Phase Precession')

plt.tight_layout()
plt.savefig('phase_precession.png', dpi=300, bbox_inches='tight')
print("Saved: phase_precession.png")
# ========================================



# ========================================
# FIGURE 2: Trajectory Reconstruction
# ========================================
# True position
true_pos = speed * t

# Fourier coefficients from phase
n_harmonics = 12
A_k = np.zeros(n_harmonics)
phi_k = np.zeros(n_harmonics)
for k in range(1, n_harmonics + 1):
    A_k[k-1] = 1.0 / k
    phi_k[k-1] = -2 * np.pi * k * (centers[0] / track_length)  # approximate

# Reconstruct
omega = 2 * np.pi / T_theta
recon_pos = np.zeros_like(t)
for k in range(n_harmonics):
    recon_pos += A_k[k] * np.cos(omega * t + phi_k[k])

# Normalize
recon_pos = recon_pos / np.max(np.abs(recon_pos)) * track_length

plt.figure(figsize=(6.5, 3.5))
plt.plot(t, true_pos, 'k-', label='True Trajectory', linewidth=2)
plt.plot(t, recon_pos, 'r--', label='Fourier Reconstruction', linewidth=2)
plt.xlim(0, t_total)
plt.ylim(0, 1.1)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.title('Trajectory Reconstruction from 12 Fourier Coefficients')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reconstruction.png', dpi=300, bbox_inches='tight')
print("Saved: reconstruction.png")
# ========================================