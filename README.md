# Phase Precession Enables Holographic Encoding in Hippocampus

**Paul Wolf (@PaulWolfCO)** | **Grok 4.1 (xAI)**  
**December 8, 2025**

## Abstract
Phase precession in the hippocampus acts as a biological Fourier transform, compressing 10-second trajectories into 120 ms theta cycles using about 12 phase coefficients. The hippocampus compresses spatiotemporal sequences into single theta cycles via phase precession - a mechanism mathematically equivalent to a Fourier transform. We show that place cell firing phases form a sparse, adaptive basis (~ 12 coefficients per cycle) that reconstructs trajectories with <5% error in silico. This compression is not mere efficiency but a holographic projection of cortical bulk (10^8 Degrees of Freedom, or DoF) onto a brainstem boundary (10^5 DoF), akin to Mach’s principle and AdS/CFT duality. 


## Files
- `main.tex`: Full LaTeX manuscript (Nature Neuroscience format)
- `phase_precession.png`: Figure 1
- `reconstruction.png`: Figure 2
- `generate_figures.py`: Python code to regenerate Figures 1 and 2.
- 'generate_figures_HOLOGRAPHIC.py' : Python code to regenerate Figure 3.
- 'generate_figure_4.py' : Python code to regenerate Figure 4.
- FIGURE_3_FINAL_HOLOGRAPHIC.png
- Figure_4_Nested_Holographic_Cascade.png

## Run
```bash
pip install numpy matplotlib
python generate_figures.py
