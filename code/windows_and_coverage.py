"""
windows_and_coverage.py

Core utilities for computing VFD φ-spaced phase centres, breathing windows,
and coverage of empirical inflection ages.

This module is designed to reproduce the main numerical results in:

    "A Technical Evaluation of φ-Spaced Phase Windows
     Against Lifespan Neuroscience Data"
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple, Sequence, Dict

import numpy as np
import pandas as pd
import pathlib


# ---------------------------------------------------------------------
# Constants (matching the technical report)
# ---------------------------------------------------------------------

PHI: float = (1.0 + 5.0 ** 0.5) / 2.0    # Golden ratio
ANCHOR_A: float = 6.0                    # years
NUM_PHASES: int = 5

W0: float = 3.0                          # baseline half-width (years)
G: float = 1.5                           # geometric expansion factor
MAX_AGE: float = 90.0                    # age range for simulations

DATA_PATH_DEFAULT = pathlib.Path(__file__).resolve().parent.parent / "data" / "extracted_transition_ages.csv"


# ---------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------

@dataclass
class PhaseWindow:
    index: int      # 1-based phase index
    centre: float   # years
    lower: float    # years
    upper: float    # years
    half_width: float  # years

    def contains(self, age: float) -> bool:
        return self.lower <= age <= self.upper


# ---------------------------------------------------------------------
# Core VFD timing model
# ---------------------------------------------------------------------

def compute_phase_centres(
    A: float = ANCHOR_A,
    phi: float = PHI,
    K: int = NUM_PHASES
) -> np.ndarray:
    """
    Compute phase centres t_k = A * phi^k for k=1..K.
    """
    k = np.arange(1, K + 1, dtype=float)
    centres = A * (phi ** k)
    return centres


def compute_window_half_widths(
    w0: float = W0,
    g: float = G,
    K: int = NUM_PHASES
) -> np.ndarray:
    """
    Compute breathing-window half-widths w_k = w0 * g^(k-1) for k=1..K.
    """
    k = np.arange(0, K, dtype=float)
    widths = w0 * (g ** k)
    return widths


def build_phase_windows(
    A: float = ANCHOR_A,
    phi: float = PHI,
    w0: float = W0,
    g: float = G,
    K: int = NUM_PHASES
) -> List[PhaseWindow]:
    """
    Construct PhaseWindow objects for the specified parameters.
    """
    centres = compute_phase_centres(A=A, phi=phi, K=K)
    half_widths = compute_window_half_widths(w0=w0, g=g, K=K)

    windows: List[PhaseWindow] = []
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


# ---------------------------------------------------------------------
# Empirical ages and coverage
# ---------------------------------------------------------------------

def load_empirical_ages(
    csv_path: pathlib.Path | None = None
) -> pd.DataFrame:
    """
    Load empirical inflection ages from CSV.

    CSV format:
        dataset,age
        BrainChart,9
        ...

    Returns:
        DataFrame with columns: ['dataset', 'age']
    """
    path = csv_path or DATA_PATH_DEFAULT
    df = pd.read_csv(path)
    df["age"] = df["age"].astype(float)
    return df


def coverage_for_ages(
    ages: Sequence[float],
    windows: Sequence[PhaseWindow]
) -> Tuple[float, np.ndarray, List[int | None]]:
    """
    Compute coverage C = (# ages inside any window) / N.

    Returns:
        coverage (float),
        covered_mask (bool array),
        assigned_windows (list of phase indices or None)
    """
    ages_arr = np.asarray(ages, dtype=float)
    N = ages_arr.shape[0]

    covered_mask = np.zeros(N, dtype=bool)
    assigned_windows: List[int | None] = [None] * N

    for i, age in enumerate(ages_arr):
        for w in windows:
            if w.contains(age):
                covered_mask[i] = True
                assigned_windows[i] = w.index
                break  # first matching window is fine

    coverage = covered_mask.mean() if N > 0 else 0.0
    return coverage, covered_mask, assigned_windows


def summarise_coverage_table(
    df: pd.DataFrame,
    windows: Sequence[PhaseWindow]
) -> pd.DataFrame:
    """
    Produce a table similar to Table 4 in the paper, assigning each age to a window.
    """
    ages = df["age"].to_numpy()
    coverage, covered_mask, assigned_windows = coverage_for_ages(ages, windows)

    df_out = df.copy()
    df_out["phase"] = assigned_windows
    df_out["covered"] = covered_mask
    df_out["coverage_fraction"] = coverage

    return df_out


# ---------------------------------------------------------------------
# Convenience CLI entry-point
# ---------------------------------------------------------------------

def main():
    """
    When run directly, print:
    - Phase window definitions
    - Coverage summary against empirical ages
    """
    print("=== VFD φ-Spaced Phase Windows ===")
    windows = build_phase_windows()
    for w in windows:
        print(
            f"P{w.index}: centre={w.centre:.2f} years, "
            f"window=[{w.lower:.1f}, {w.upper:.1f}], "
            f"half-width={w.half_width:.2f}"
        )

    print("\n=== Empirical inflection age coverage ===")
    df = load_empirical_ages()
    table = summarise_coverage_table(df, windows)
    coverage = table["coverage_fraction"].iloc[0] if len(table) > 0 else 0.0
    print(table[["dataset", "age", "phase", "covered"]])
    print(f"\nCoverage C_phi = {coverage:.4f} "
          f"({int(coverage * len(table))} of {len(table)} ages covered)")


if __name__ == "__main__":
    main()
