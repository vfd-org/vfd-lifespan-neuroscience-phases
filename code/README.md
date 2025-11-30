# VFD Phase Windows Analysis Code

This directory contains Python code to reproduce the numerical results from:

**"A Technical Evaluation of φ-Spaced Phase Windows Against Lifespan Neuroscience Data"**

VFD Institute Technical Report

---

## Files

| File | Description |
|------|-------------|
| `windows_and_coverage.py` | Core module: phase window computation, coverage metrics |
| `monte_carlo_baselines.py` | Random-age and random-window Monte Carlo simulations |
| `ratio_scan.py` | Scan alternative scaling ratios r ∈ [1.4, 1.9] |
| `analysis.ipynb` | Jupyter notebook reproducing all key results |

---

## Requirements

```
numpy
pandas
matplotlib
```

Install with:
```bash
pip install numpy pandas matplotlib
```

---

## Quick Start

### 1. View phase windows and coverage

```bash
cd code
python windows_and_coverage.py
```

Output:
```
=== VFD φ-Spaced Phase Windows ===
P1: centre=9.71 years, window=[6.7, 12.7], half-width=3.00
P2: centre=15.71 years, window=[11.2, 20.2], half-width=4.50
...

=== Empirical inflection age coverage ===
Coverage C_phi = 0.9375 (15 of 16 ages covered)
```

### 2. Run Monte Carlo baselines

```bash
python monte_carlo_baselines.py
```

Output:
```
Empirical VFD coverage C_phi = 0.9375

--- Random-age baseline ---
Mean coverage (random ages): 0.83 ± 0.09
P(C >= C_phi) under random ages = 0.22

--- Random-window baseline ---
Mean coverage (random windows): 0.63 ± 0.12
P(C >= C_phi) under random windows = 0.055
```

### 3. Run ratio scan and generate figure

```bash
python ratio_scan.py
```

This produces `coverage_vs_ratio.png` and prints:
```
Best ratio in scan: r ≈ 1.63 with coverage C(r) = 0.9375
Effective band (C(r) >= C_phi): [1.500, 1.700]
```

### 4. Run full analysis notebook

```bash
jupyter notebook analysis.ipynb
```

Or in VS Code, open `analysis.ipynb` and run all cells.

---

## Key Results

| Measure | Value |
|---------|-------|
| VFD coverage (C_φ) | 0.94 (15/16) |
| Random-age mean | 0.83 |
| Random-age p-value | 0.22 |
| Random-window mean | 0.63 |
| Random-window p-value | 0.055 |
| Best ratio | r ≈ 1.63 |
| Effective band | [1.5, 1.7] |

---

## Model Parameters

```python
PHI = 1.6180339887    # Golden ratio
ANCHOR_A = 6.0        # years
NUM_PHASES = 5
W0 = 3.0              # baseline half-width (years)
G = 1.5               # geometric expansion factor
```

---

## Data

Empirical inflection ages are stored in `../data/extracted_transition_ages.csv`:

| Dataset | Ages (years) |
|---------|--------------|
| BrainChart | 9, 20, 30, 65 |
| ENIGMA | 8, 15, 28, 62 |
| MEG | 12, 18, 40, 70 |
| Cambridge | 9, 32, 66, 83 |

---

## License

See repository root for license information.
