# VFD φ-Spaced Phase Windows: Lifespan Neuroscience Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository contains the complete reproducible analysis pipeline for:

**"A Technical Evaluation of φ-Spaced Phase Windows Against Lifespan Neuroscience Data"**

*An Exploratory Analysis within the Vibrational Field Dynamics Framework*

**Author:** Lee Smart
**Institution:** Vibrational Field Dynamics Institute
**Contact:** contact@vibrationalfielddynamics.org
**Twitter/X:** [@vfd_org](https://twitter.com/vfd_org)

## Abstract

This exploratory study evaluates whether a minimal geometric timing model—employing φ-scaled (golden ratio) phase windows—aligns with empirically observed neurobiological reorganisation periods across the human lifespan. The model generates five phase windows from a single recursive formula with phase centres determined *a priori*. VFD phase windows achieved 93.75% coverage of empirical transition ages (15 of 16 datapoints) extracted from four independent large-scale neuroimaging datasets.

## Repository Structure

```
vfd-lifespan-neuroscience-phases/
├── README.md                           # This file
├── CITATION.cff                        # Citation metadata
├── CONTRIBUTING.md                     # Contribution guidelines
├── LICENSE                             # MIT License
├── .gitignore                          # Git ignore rules
│
├── paper/
│   └── vfd_phi_phase_windows_paper_final.tex   # LaTeX source
│
├── code/
│   ├── windows_and_coverage.py         # Core VFD model implementation
│   ├── monte_carlo_baselines.py        # Random-age and random-window baselines
│   ├── ratio_scan.py                   # Alternative scaling ratio analysis
│   ├── linear_exponential_baselines.py # Linear and exponential baselines
│   ├── analysis.ipynb                  # Jupyter notebook (all analyses)
│   └── coverage_vs_ratio.png           # Generated figure
│
└── data/
    ├── extracted_transition_ages.csv   # 16 empirical inflection ages
    ├── extraction_notes.md             # Data extraction methodology
    ├── validation_summary.md           # Validated numerical results
    └── digitised_curves/
        ├── brainchart_grey_matter_volume.csv
        ├── brainchart_white_matter_volume.csv
        ├── enigma_cortical_thickness.csv
        ├── meg_alpha_power.csv
        ├── meg_beta_power.csv
        ├── meg_gamma_power.csv
        ├── cambridge_global_efficiency.csv
        └── cambridge_modularity.csv
```

## Quick Start

### Prerequisites

```bash
pip install numpy matplotlib pandas seaborn jupyter
```

### Running the Analysis

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vfd-org/vfd-lifespan-neuroscience-phases.git
   cd vfd-lifespan-neuroscience-phases
   ```

2. **Run individual scripts:**
   ```bash
   cd code
   python windows_and_coverage.py      # Core coverage calculation
   python monte_carlo_baselines.py     # Monte Carlo simulations
   python linear_exponential_baselines.py  # Alternative baselines
   python ratio_scan.py                # Ratio scan analysis
   ```

3. **Or run the complete analysis notebook:**
   ```bash
   jupyter notebook analysis.ipynb
   ```

## Validated Results

All numerical results are deterministically reproducible with fixed random seeds:

| Metric | Value |
|--------|-------|
| VFD Coverage (C_φ) | 0.9375 (15/16) |
| Random-age baseline mean | 0.8324 |
| Random-age p-value | 0.2234 |
| Random-window baseline mean | 0.5150 |
| Random-window p-value | 0.0127 |
| Linear spacing coverage | 0.6875 (11/16) |
| Exponential spacing coverage* | 0.9375 (15/16) |
| Best performing ratio | r ≈ 1.63 |
| Effective ratio band | [1.56, 1.79] |

*Range-matched; not an independent baseline (r_exp ≈ 1.60 ≈ φ)

## Reproducibility

**Fixed Random Seeds:**
- Random-age baseline: `12345`
- Random-window baseline: `12346`
- Monte Carlo iterations: 20,000

All scripts produce identical output on each execution.

## Key Findings

1. **High coverage:** VFD phase windows capture 93.75% of empirical neurodevelopmental transitions
2. **Significant vs. random placement:** p = 0.0127 for random-window baseline
3. **φ is not uniquely optimal:** A band of ratios [1.56, 1.79] achieves comparable coverage
4. **Logarithmic-geometric scaling** appears to be the operative principle, not φ specifically

## Citation

If you use this work, please cite:

```bibtex
@techreport{smart2025vfd,
  author       = {Smart, Lee},
  title        = {A Technical Evaluation of φ-Spaced Phase Windows Against Lifespan Neuroscience Data},
  institution  = {Vibrational Field Dynamics Institute},
  year         = {2025},
  type         = {Technical Report},
  url          = {https://github.com/vfd-org/vfd-lifespan-neuroscience-phases}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Email:** contact@vibrationalfielddynamics.org
- **Twitter/X:** [@vfd_org](https://twitter.com/vfd_org)
- **GitHub:** [vfd-org](https://github.com/vfd-org)

---

**Vibrational Field Dynamics Institute**
*Advancing geometric frameworks for understanding biological organisation*
