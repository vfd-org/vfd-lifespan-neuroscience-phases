"""
linear_exponential_baselines.py

Compute coverage for linear and exponential baseline spacing models.
"""

from __future__ import annotations

import numpy as np

from windows_and_coverage import (
    PhaseWindow,
    compute_window_half_widths,
    load_empirical_ages,
    coverage_for_ages,
    W0,
    G,
    NUM_PHASES,
)


def build_linear_windows() -> list[PhaseWindow]:
    """
    Linear spacing: centres at 10, 25, 40, 55, 70 years.
    t_k = 10 + (k-1) * 15
    """
    centres = [10 + (k - 1) * 15 for k in range(1, NUM_PHASES + 1)]
    half_widths = compute_window_half_widths(w0=W0, g=G, K=NUM_PHASES)

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
    return windows


def build_exponential_windows() -> list[PhaseWindow]:
    """
    Exponential spacing: t_k = 10 * r_exp^(k-1)
    where r_exp = (66/10)^(1/4) ≈ 1.60
    """
    r_exp = (66.0 / 10.0) ** 0.25  # ≈ 1.60
    centres = [10.0 * (r_exp ** (k - 1)) for k in range(1, NUM_PHASES + 1)]
    half_widths = compute_window_half_widths(w0=W0, g=G, K=NUM_PHASES)

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
    return windows


def main():
    """
    Compute coverage for linear and exponential baselines.
    """
    df = load_empirical_ages()
    ages = df["age"].to_numpy()

    # Linear baseline
    print("=== Linear Baseline ===")
    linear_windows = build_linear_windows()
    for w in linear_windows:
        print(f"  P{w.index}: centre={w.centre:.1f}, window=[{w.lower:.1f}, {w.upper:.1f}]")

    C_linear, covered_linear, _ = coverage_for_ages(ages, linear_windows)
    print(f"\nLinear coverage: {C_linear:.4f} ({int(C_linear * len(ages))}/16)")

    # Exponential baseline
    print("\n=== Exponential Baseline ===")
    exp_windows = build_exponential_windows()
    for w in exp_windows:
        print(f"  P{w.index}: centre={w.centre:.1f}, window=[{w.lower:.1f}, {w.upper:.1f}]")

    C_exp, covered_exp, _ = coverage_for_ages(ages, exp_windows)
    print(f"\nExponential coverage: {C_exp:.4f} ({int(C_exp * len(ages))}/16)")

    # Summary
    print("\n=== Summary ===")
    print(f"Linear baseline:      {C_linear:.4f} ({int(C_linear * len(ages))}/16)")
    print(f"Exponential baseline: {C_exp:.4f} ({int(C_exp * len(ages))}/16)")
    print("\nNote: Exponential baseline is range-matched (r_exp ≈ 1.60 ≈ φ),")
    print("so it achieves identical coverage to VFD. This is expected.")


if __name__ == "__main__":
    main()
