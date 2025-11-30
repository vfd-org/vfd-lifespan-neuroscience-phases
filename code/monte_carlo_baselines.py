"""
monte_carlo_baselines.py

Monte Carlo baselines for the VFD φ-spaced phase window model:

1) Random-age baseline:
   - Ages sampled uniformly from [0, MAX_AGE]
   - Windows fixed to VFD configuration

2) Random-window baseline:
   - Empirical ages fixed
   - Window widths fixed
   - Window centres randomised (and sorted)

Reproducibility: All simulations use fixed seeds for deterministic results.
"""

from __future__ import annotations

import numpy as np

# ---------------------------------------------------------------------
# Fixed random seed for reproducibility
# ---------------------------------------------------------------------
GLOBAL_SEED: int = 12345

from windows_and_coverage import (
    build_phase_windows,
    compute_window_half_widths,
    load_empirical_ages,
    coverage_for_ages,
    MAX_AGE,
    NUM_PHASES,
    W0,
    G,
    PhaseWindow,
)


def random_age_baseline(
    n_iter: int = 20_000,
    n_ages: int = 16,
    seed: int = GLOBAL_SEED,
) -> dict:
    """
    Random-age baseline:
    - Ages ~ Uniform(0, MAX_AGE)
    - Windows = fixed VFD configuration
    """
    rng = np.random.default_rng(seed)

    windows = build_phase_windows()
    coverages = np.zeros(n_iter, dtype=float)

    for i in range(n_iter):
        random_ages = rng.uniform(0.0, MAX_AGE, size=n_ages)
        C, _, _ = coverage_for_ages(random_ages, windows)
        coverages[i] = C

    results = {
        "mean_coverage": float(coverages.mean()),
        "std_coverage": float(coverages.std(ddof=1)),
        "all_coverages": coverages,
    }
    return results


def random_window_baseline(
    n_iter: int = 20_000,
    seed: int = GLOBAL_SEED + 1,  # Use different seed from random_age for independence
) -> dict:
    """
    Random-window baseline:
    - Ages fixed to empirical set
    - Window widths fixed to breathing-window widths
    - Window centres randomised uniformly and sorted
    """
    rng = np.random.default_rng(seed)

    df = load_empirical_ages()
    ages = df["age"].to_numpy()
    n_ages = ages.shape[0]

    half_widths = compute_window_half_widths(w0=W0, g=G, K=NUM_PHASES)
    coverages = np.zeros(n_iter, dtype=float)

    for i in range(n_iter):
        centres = np.sort(rng.uniform(0.0, MAX_AGE, size=NUM_PHASES))

        windows = []
        for idx, (c, h) in enumerate(zip(centres, half_widths), start=1):
            windows.append(
                PhaseWindow(
                    index=idx,
                    centre=float(c),
                    lower=float(c - h),
                    upper=float(c + h),
                    half_width=float(h),
                )
            )

        C, _, _ = coverage_for_ages(ages, windows)
        coverages[i] = C

    results = {
        "mean_coverage": float(coverages.mean()),
        "std_coverage": float(coverages.std(ddof=1)),
        "all_coverages": coverages,
    }
    return results


def main():
    """
    Run baselines and print summary statistics and empirical p-values.
    """
    print("=== Monte Carlo Baselines for VFD Phase Windows ===")

    # Compute empirical VFD coverage
    windows = build_phase_windows()
    df = load_empirical_ages()
    ages = df["age"].to_numpy()
    C_phi, _, _ = coverage_for_ages(ages, windows)
    print(f"Empirical VFD coverage C_phi = {C_phi:.4f}")

    # Random-age baseline
    print("\n--- Random-age baseline ---")
    ra = random_age_baseline()
    cov = ra["all_coverages"]
    p_ge = np.mean(cov >= C_phi)
    print(f"Mean coverage (random ages): {ra['mean_coverage']:.4f} "
          f"± {ra['std_coverage']:.4f}")
    print(f"P(C >= C_phi) under random ages = {p_ge:.4f}")

    # Random-window baseline
    print("\n--- Random-window baseline ---")
    rw = random_window_baseline()
    cov_w = rw["all_coverages"]
    p_ge_w = np.mean(cov_w >= C_phi)
    print(f"Mean coverage (random windows): {rw['mean_coverage']:.4f} "
          f"± {rw['std_coverage']:.4f}")
    print(f"P(C >= C_phi) under random windows = {p_ge_w:.4f}")

    print(f"\nReproducibility: Seeds used = {GLOBAL_SEED} (random-age), "
          f"{GLOBAL_SEED + 1} (random-window)")


if __name__ == "__main__":
    main()
