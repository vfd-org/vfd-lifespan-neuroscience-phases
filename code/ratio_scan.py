"""
ratio_scan.py

Scan alternative geometric scaling ratios r in [1.4, 1.9]
and compute coverage for each using:

    t_k(r) = 6 * r^k,  k = 1..5

with the same breathing-window half-widths used for the φ model.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from windows_and_coverage import (
    PhaseWindow,
    compute_window_half_widths,
    load_empirical_ages,
    coverage_for_ages,
    build_phase_windows,
    W0,
    G,
    NUM_PHASES,
    PHI,
    ANCHOR_A,
)


def build_windows_for_ratio(
    r: float,
    A: float = ANCHOR_A,
    w0: float = W0,
    g: float = G,
    K: int = NUM_PHASES,
) -> list[PhaseWindow]:
    """
    Build phase windows for an arbitrary scaling ratio r.

    t_k = A * r^k
    half-widths w_k = w0 * g^(k-1)
    """
    k = np.arange(1, K + 1, dtype=float)
    centres = A * (r ** k)
    half_widths = compute_window_half_widths(w0=w0, g=g, K=K)

    windows: list[PhaseWindow] = []
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
    return windows


def scan_ratios(
    r_min: float = 1.4,
    r_max: float = 1.9,
    n_points: int = 51,
) -> dict:
    """
    Scan scaling ratios r in [r_min, r_max] and compute coverage for each.

    Returns:
        dict with:
            'ratios' (np.ndarray),
            'coverages' (np.ndarray),
            'best_r' (float),
            'best_coverage' (float)
    """
    df = load_empirical_ages()
    ages = df["age"].to_numpy()

    ratios = np.linspace(r_min, r_max, n_points)
    coverages = np.zeros_like(ratios)

    for i, r in enumerate(ratios):
        windows = build_windows_for_ratio(r)
        C, _, _ = coverage_for_ages(ages, windows)
        coverages[i] = C

    best_idx = int(np.argmax(coverages))
    best_r = float(ratios[best_idx])
    best_coverage = float(coverages[best_idx])

    return {
        "ratios": ratios,
        "coverages": coverages,
        "best_r": best_r,
        "best_coverage": best_coverage,
    }


def plot_ratio_scan(results: dict, outfile: str = "coverage_vs_ratio.png"):
    """
    Plot coverage vs scaling ratio and save as PNG.
    """
    ratios = results["ratios"]
    coverages = results["coverages"]

    plt.figure(figsize=(7.0, 4.5))
    plt.plot(ratios, coverages, marker="o", markersize=4, linewidth=1)
    plt.axvline(PHI, color="red", linestyle="--", alpha=0.7, label=f"φ ≈ {PHI:.3f}")
    plt.xlabel("Scaling ratio r")
    plt.ylabel("Coverage C(r)")
    plt.title("Coverage of empirical ages as a function of scaling ratio r")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(outfile, dpi=300)
    plt.close()
    print(f"Saved ratio scan plot to {outfile}")


def main():
    """
    Run ratio scan and print key summary values.
    """
    df = load_empirical_ages()
    ages = df["age"].to_numpy()

    # Baseline φ coverage
    windows_phi = build_phase_windows()
    C_phi, _, _ = coverage_for_ages(ages, windows_phi)
    print(f"VFD φ coverage C_phi = {C_phi:.4f}")

    # Ratio scan
    results = scan_ratios()
    ratios = results["ratios"]
    coverages = results["coverages"]
    best_r = results["best_r"]
    best_cov = results["best_coverage"]

    print(f"\nBest ratio in scan: r ≈ {best_r:.4f} "
          f"with coverage C(r) = {best_cov:.4f}")

    # Effective band: coverage >= C_phi
    mask = coverages >= C_phi
    if mask.any():
        effective_min = float(ratios[mask].min())
        effective_max = float(ratios[mask].max())
        print(f"Effective band (C(r) >= C_phi): "
              f"[{effective_min:.3f}, {effective_max:.3f}]")
    else:
        print("No ratios achieved coverage >= C_phi in the scanned range.")

    # Save plot
    plot_ratio_scan(results)


if __name__ == "__main__":
    main()
