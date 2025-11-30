# Data Extraction Notes

## Overview

This document describes the sources, methods, and limitations of the empirical data used in:

**"A Technical Evaluation of φ-Spaced Phase Windows Against Lifespan Neuroscience Data"**

VFD Institute Technical Report

---

## Source Datasets

### 1. BrainChart Consortium (Bethlehem et al., 2022)

**Citation:**
> Bethlehem, R. A., Seidlitz, J., White, S. R., Vogel, J. W., Anderson, K. M., Adamson, C., ... & Alexander-Bloch, A. F. (2022). Brain charts for the human lifespan. *Nature*, 604(7906), 525-533.

**DOI:** [10.1038/s41586-022-04554-y](https://doi.org/10.1038/s41586-022-04554-y)

**Data Resource:** [brainchart.io](https://brainchart.io)

**Sample Size:** 123,984 MRI scans from 101,457 participants (115 days post-conception to 100 years)

**Measures Used:**
- Grey matter volume (GMV)
- White matter volume (WMV)
- Total brain volume

**Figure References:**
- Figure 1: Lifespan centile charts for brain morphometry
- Extended Data Figure 2: Regional grey matter trajectories

**Key Trajectory Findings from Literature:**
- Grey matter volume peaks at approximately 5.9 years for cortical GM
- Subcortical grey matter peaks at 14.4 years
- White matter peaks at approximately 28.7 years
- Accelerated atrophy begins after age 60

**Extracted Inflection Ages:**
| Age | Neurobiological Event |
|-----|----------------------|
| 9 | Rate change in grey matter decline post-childhood peak |
| 20 | End of major myelination/pruning phase |
| 30 | Onset of volume stabilisation plateau |
| 65 | Acceleration of age-related atrophy |

---

### 2. ENIGMA Cortical Thickness (Frangou et al., 2022)

**Citation:**
> Frangou, S., Modabbernia, A., Williams, S. C., Papachristou, E., Doucet, G. E., Agartz, I., ... & Dima, D. (2022). Cortical thickness across the lifespan: Data from 17,075 healthy individuals aged 3-90 years. *Human Brain Mapping*, 43(1), 431-451.

**DOI:** [10.1002/hbm.25364](https://doi.org/10.1002/hbm.25364)

**Sample Size:** 17,075 healthy individuals aged 3-90 years

**Measures Used:**
- Mean cortical thickness across 34 bilateral ROIs
- Regional cortical thickness trajectories

**Figure References:**
- Figure 2: Cortical thickness trajectories across lifespan
- Figure 3: Regional variation in thickness trajectories

**Key Trajectory Findings from Literature:**
- Cortical thickness peaks in childhood (highest values age 3-5)
- Steep decrease during first 2-3 decades
- Gradual monotonic decrease thereafter
- Regional heterochronicity (prefrontal matures later than sensory)

**Extracted Inflection Ages:**
| Age | Neurobiological Event |
|-----|----------------------|
| 8 | Transition from thickening to thinning in most regions |
| 15 | Acceleration of adolescent cortical thinning |
| 28 | Deceleration; entry to slow adult decline |
| 62 | Acceleration of senescent thinning |

---

### 3. MEG Oscillatory Power (Multiple Sources)

**Primary Citation:**
> Stier, C., Braun, U., & Bhattacharjee, S. (2024). Lifespan trajectories of spectral power in magnetoencephalography. *NeuroImage*, 285, 120472.

**Supporting Citations:**
> Sahoo, B., et al. (2020). Gamma oscillations weaken with age in healthy elderly in human EEG. *NeuroImage*, 215, 116826.

> Rué-Queralt, J., et al. (2023). Adult lifespan trajectories of neuromagnetic signals and interrelations with cortical thickness. *NeuroImage*, 281, 120361.

**DOI (Stier et al.):** [10.1016/j.neuroimage.2023.120472](https://doi.org/10.1016/j.neuroimage.2023.120472)

**Sample Size:** Varies by study (largest: n=434, ages 6-84)

**Measures Used:**
- Alpha power (8-12 Hz)
- Beta power (13-30 Hz)
- Gamma power (30-100 Hz)
- Theta power (4-8 Hz)

**Key Trajectory Findings from Literature:**
- Lower frequencies (delta, theta) decrease with age
- Alpha peaks in childhood/early adolescence, then declines
- Beta increases with age (possible compensatory mechanism)
- Gamma shows complex trajectory with decline in later life
- Spectral changes pivot around alpha band

**Extracted Inflection Ages:**
| Age | Neurobiological Event |
|-----|----------------------|
| 12 | Alpha power peak; transition to adult rhythmicity |
| 18 | Beta power stabilisation |
| 40 | Gamma power decline onset |
| 70 | Broad-spectrum power reduction acceleration |

---

### 4. Cambridge Connectome Topology (Betzel et al., 2014; Zhao et al., 2015; 2025 update)

**Primary Citations:**
> Betzel, R. F., Byrge, L., He, Y., Goñi, J., Zuo, X. N., & Sporns, O. (2014). Changes in structural and functional connectivity among resting-state networks across the human lifespan. *NeuroImage*, 102, 345-357.

> Zhao, T., Cao, M., Niu, H., Zuo, X. N., Evans, A., He, Y., ... & Shu, N. (2015). Age-related changes in the topological organization of the white matter structural connectome across the human lifespan. *Human Brain Mapping*, 36(10), 3777-3792.

**Recent Validation:**
> (2025). Topological turning points across the human lifespan. *Nature Communications*.

**DOI (Betzel):** [10.1016/j.neuroimage.2014.08.026](https://doi.org/10.1016/j.neuroimage.2014.08.026)

**DOI (Zhao):** [10.1002/hbm.22877](https://doi.org/10.1002/hbm.22877)

**Sample Size:**
- Zhao et al.: 113 participants (ages 9-85)
- 2025 study: N=4,216 (ages 0-90)

**Measures Used:**
- Global efficiency
- Network modularity
- Hub organization
- Rich club coefficients

**Key Trajectory Findings from Literature:**
- Global efficiency follows inverted U-shape, peak ~30 years
- Modularity peaks in young adulthood
- Network segregation decreases with age
- Hub degradation accelerates in late life
- Four major topological turning points identified: ~9, 32, 66, 83 years

**Extracted Inflection Ages:**
| Age | Neurobiological Event |
|-----|----------------------|
| 9 | Emergence of modular organisation |
| 32 | Peak global efficiency |
| 66 | Accelerated hub degradation |
| 83 | Network fragmentation onset |

---

## Extraction Methodology

### Curve Digitisation Process

1. **Source Acquisition**: Published figures were obtained from journal websites, PMC, or preprint servers where available.

2. **Representative Curves**: Where direct digitisation was not possible, representative curves were constructed based on:
   - Quantitative values reported in paper text
   - Trajectory descriptions in results sections
   - Supplementary data tables
   - Known neuroscience literature consensus

3. **Inflection Point Estimation**: For each curve:
   - Visual inspection of apparent rate changes
   - First derivative estimation (where data density permitted)
   - Cross-referencing with ages reported in original papers
   - Literature consensus values for well-established transitions

### Limitations and Precision Warnings

**Critical Caveats:**

1. **Visual Extraction Uncertainty**: Inflection ages were estimated visually from published figures, not computed from raw data. Different analysts might extract slightly different values (±2-3 years uncertainty).

2. **Representative vs. Digitised**: Some curves are "representative" reconstructions based on literature descriptions rather than point-by-point digitisation from figures.

3. **Cross-Study Variation**: Different studies use different samples, methods, and age ranges. Extracted ages represent approximate central tendencies, not precise population parameters.

4. **Publication Bias**: Consortium studies may report "round" ages or emphasize transitions that match prior expectations.

5. **Heterogeneous Measures**: The four datasets measure fundamentally different neurobiological properties. Alignment of inflection ages may or may not reflect common underlying processes.

6. **Interpolation Effects**: Curves were smoothed/interpolated to standard age intervals, which may shift apparent inflection points.

### Reproducibility Notes

- All digitised curve files include a `notes` column indicating key inflection points
- Ages marked as "INFLECTION" in notes correspond to the 16 values in `extracted_transition_ages.csv`
- Curves can be re-analysed with different smoothing parameters or inflection detection methods

---

## Summary Table: Extracted Inflection Ages

| Dataset | Age 1 | Age 2 | Age 3 | Age 4 |
|---------|-------|-------|-------|-------|
| BrainChart | 9 | 20 | 30 | 65 |
| ENIGMA | 8 | 15 | 28 | 62 |
| MEG | 12 | 18 | 40 | 70 |
| Cambridge | 9 | 32 | 66 | 83 |

**Total: 16 inflection ages**

---

## File Manifest

```
data/
├── extracted_transition_ages.csv          # Final 16 inflection ages
├── extraction_notes.md                     # This file
└── digitised_curves/
    ├── brainchart_grey_matter_volume.csv  # GMV trajectory
    ├── brainchart_white_matter_volume.csv # WMV trajectory
    ├── enigma_cortical_thickness.csv      # CT trajectory
    ├── meg_alpha_power.csv                # Alpha power
    ├── meg_beta_power.csv                 # Beta power
    ├── meg_gamma_power.csv                # Gamma power
    ├── cambridge_global_efficiency.csv    # Network efficiency
    └── cambridge_modularity.csv           # Network modularity
```

---

## Contact

For questions about data extraction methodology, contact the VFD Institute.

**Last Updated:** November 2024
