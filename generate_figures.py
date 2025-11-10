# generate_figures_TRUTH.py
import numpy as np
import matplotlib.pyplot as plt

# === 12 PLACE CELLS ===
n_cells = 12
centers = np.linspace(0.1, 0.9, n_cells)  # True positions
phases_deg = 300 - 240 * centers
phases_rad = np.radians(phases_deg)

# === FOURIER FIT ===
n_harm = 12
A = np.zeros(n_harm + 1)
B = np.zeros(n_harm + 1)

# DC term
A[0] = np.mean(centers)

# AC terms
for k in range(1, n_harm + 1):
    cos_basis = np.cos(k * phases_rad)
    sin_basis = np.sin(k * phases_rad)
    A[k] = 2 * np.mean(centers * cos_basis)
    B[k] = 2 * np.mean(centers * sin_basis)

# === RECONSTRUCT AT SAME POINTS ===
recon = np.zeros_like(centers)
for k in range(n_harm + 1):
    if k == 0:
        recon += A[0]
    else:
        recon += A[k] * np.cos(k * phases_rad) + B[k] * np.sin(k * phases_rad)

# === PLOT ===
plt.figure(figsize=(6.5, 3.5))
plt.plot(centers, centers, 'k-', label='True Position', linewidth=2)
plt.plot(centers, recon, 'ro', label='Fourier Reconstruction', markersize=8)
plt.xlabel('True Position (m)')
plt.ylabel('Reconstructed Position (m)')
plt.title('Fourier Reconstruction from 12 Phase Samples')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('reconstruction_TRUTH.png', dpi=300)
print(f"MSE: {np.mean((centers - recon)**2):.2e}")