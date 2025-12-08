# Phase Precession Enables Holographic Encoding in Hippocampus

**Paul Wolf (@PaulWolfCO)** | **Grok 4.1 (xAI)**  
**December 8, 2025**

## Abstract
The hippocampus encodes spatial position through place cells, whose spiking is modulated by theta oscillations and phase precession—a progressive shift in spike timing relative to the theta cycle as an animal traverses a place field. Here, we propose that phase precession implements a holographic Fourier encoding of position, transforming linear spatial trajectories into distributed, interference-based representations across neural ensembles. Drawing on holographic principles, we model place cell activity as superpositions of frequency-modulated waves, where theta phase advances enable constructive interference at specific locations, akin to a neural diffraction grating.  This framework integrates across hippocampal layers: entorhinal grid inputs provide low-frequency spatial priors to CA3, while CA1 output layers refine high-frequency details via recurrent feedback. Critically, phase precession enforces Markov blankets at layer boundaries, preserving statistical independence between internal states (e.g., position estimates) and external sensory flows, thus enabling robust inference under uncertainty.  Simulations demonstrate that this encoding supports compression-resistant memory storage and rapid pattern completion, outperforming traditional rate-based models in noisy environments. This model offers a unified account of phase precession's computational role, bridging neural dynamics with information-theoretic holography.

## Files
- `Phase_Precession_Enables_Holographic_Encoding_in_Hippocampus.pdf`: PDF version of paper with figures.
- `main.tex`: Full LaTeX manuscript 
- `phase_precession.png`: Figure 1
- `reconstruction.png`: Figure 2
- `generate_figures.py`: Python code to regenerate Figures 1 and 2.
- `generate_figures_HOLOGRAPHIC.py` : Python code to regenerate Figure 3.
- `generate_figure_4.py` : Python code to regenerate Figure 4.
- `FIGURE_3_FINAL_HOLOGRAPHIC.png`: Figure 3
- `Figure_4_Nested_Holographic_Cascade.png`: Figure 4

## Run
```bash
pip install numpy matplotlib
python generate_figures.py
python generate_figures_HOLOGRAPHIC.py
python Figure_4_Nested_Holographic_Cascade.png