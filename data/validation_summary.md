# Validation Summary

## Canonical Results (Final, Reproducible)

All Python scripts executed with fixed random seeds for full reproducibility.

**Seeds used:**
- Random-age baseline: `12345`
- Random-window baseline: `12346`
- Iterations: 20,000 per baseline

---

## Final Numerical Results

### Core VFD Coverage

| Metric | Value |
|--------|-------|
| VFD Coverage (C_φ) | **0.9375** |
| Ages Covered | 15 of 16 |
| Age Missed | 83 (Cambridge network fragmentation) |

### Monte Carlo Baselines

| Baseline | Mean Coverage | P(C ≥ C_φ) |
|----------|---------------|------------|
| Random-age | **0.8324** | **0.2234** |
| Random-window | **0.5150** | **0.0127** |

### Ratio Scan

| Metric | Value |
|--------|-------|
| Best ratio | **r ≈ 1.63** |
| Best coverage | 1.0000 |
| φ ≈ 1.618 coverage | 0.9375 |
| Effective band (C ≥ C_φ) | **[1.56, 1.79]** |

### Alternative Baselines

| Baseline | Coverage | Ages Covered |
|----------|----------|--------------|
| Linear | **0.6875** | 11/16 |
| Exponential (range-matched) | **0.9375** | 15/16 |

---

## Notes on Exponential Baseline

The exponential baseline uses the formula:
```
t_k = 10 × r_exp^(k-1),  r_exp = (66/10)^(1/4) ≈ 1.60
```

This produces centres at [10.0, 16.0, 25.7, 41.2, 66.0] years, which are nearly identical to the VFD φ-based centres [9.7, 15.7, 25.4, 41.1, 66.5]. Therefore:

1. **The exponential baseline achieves the same coverage (0.9375) as VFD.**
2. **It is not an independent baseline** but rather a sanity check confirming that ratio ≈ 1.6 produces high coverage.
3. **The narrative relies primarily on random-window and linear baselines** for comparison, as these provide genuinely different window configurations.

---

## Interpretation

1. **VFD coverage (0.9375)** significantly exceeds random-window placement (mean 0.5150, p = 0.0127).
2. **VFD coverage** exceeds linear spacing (0.6875) by a substantial margin.
3. **The effective ratio band [1.56, 1.79]** confirms that φ ≈ 1.618 sits within a broader band of effective scaling ratios—logarithmic-geometric scaling is the operative principle, not φ uniquely.
4. **The random-age baseline** (mean 0.8324, p = 0.2234) does not reach significance, reflecting the wide cumulative window span.

---

## File Locations

| Result | File |
|--------|------|
| VFD Coverage | `code/windows_and_coverage.py` |
| MC Baselines | `code/monte_carlo_baselines.py` |
| Ratio Scan | `code/ratio_scan.py` |
| Alt Baselines | `code/linear_exponential_baselines.py` |
| Analysis Notebook | `code/analysis.ipynb` |
| Ratio Plot | `code/coverage_vs_ratio.png` |

---

**Validation Date:** November 2024
**Seeds:** 12345, 12346
**Iterations:** 20,000
