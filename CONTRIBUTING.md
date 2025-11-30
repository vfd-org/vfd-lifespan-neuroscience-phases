# Contributing to VFD Lifespan Neuroscience Phases

Thank you for your interest in contributing to this research project. This document outlines guidelines for contributing to the reproducibility and extension of this analysis.

## Overview

This repository supports a technical report evaluating φ-spaced phase windows against lifespan neuroscience data. Contributions that enhance reproducibility, extend the analysis, or improve documentation are welcome.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- Git

### Setting Up the Development Environment

```bash
# Clone the repository
git clone https://github.com/vfd-org/vfd-lifespan-neuroscience-phases.git
cd vfd-lifespan-neuroscience-phases

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install numpy matplotlib pandas seaborn jupyter
```

### Running the Analysis

Verify your setup by running all scripts:

```bash
cd code
python windows_and_coverage.py
python monte_carlo_baselines.py
python linear_exponential_baselines.py
python ratio_scan.py
```

Expected outputs should match the values in `data/validation_summary.md`.

## Contribution Guidelines

### Types of Contributions

1. **Bug fixes**: Corrections to code errors or documentation typos
2. **Reproducibility improvements**: Enhancements to make the analysis easier to reproduce
3. **Extended analyses**: New baselines, alternative parameterisations, or additional datasets
4. **Documentation**: Improved explanations, examples, or methodology descriptions

### Contribution Process

1. **Fork the repository** and create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines below

3. **Verify reproducibility**: Ensure all scripts still produce the validated results:
   - VFD Coverage = 0.9375
   - Random-age p-value = 0.2234
   - Random-window p-value = 0.0127

4. **Update documentation** if your changes affect usage or results

5. **Submit a pull request** with a clear description of your changes

### Code Style

- Follow PEP 8 for Python code
- Use descriptive variable names
- Include docstrings for functions
- Comment complex logic
- Preserve fixed random seeds for reproducibility

### Reproducibility Requirements

**Critical**: All contributions must maintain reproducibility. This means:

- **Do not change random seeds** unless explicitly extending the analysis
- **Document any new seeds** in `data/validation_summary.md`
- **Verify outputs** match expected values before submitting
- **Use fixed seeds** for any new Monte Carlo simulations

### Testing Your Changes

Run the full validation protocol:

```bash
cd code
python windows_and_coverage.py        # Should output: Coverage = 0.9375
python monte_carlo_baselines.py       # Should output: p-values as documented
python linear_exponential_baselines.py
python ratio_scan.py                  # Should output: Best ratio ≈ 1.63
```

## Reporting Issues

If you find a bug or have a suggestion:

1. Check existing issues to avoid duplicates
2. Create a new issue with:
   - Clear title
   - Detailed description
   - Steps to reproduce (if applicable)
   - Expected vs. actual behaviour

## Questions and Discussion

For questions about the methodology or theoretical framework:
- Email: contact@vibrationalfielddynamics.org
- Twitter/X: [@vfd_org](https://twitter.com/vfd_org)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Acknowledgements

We appreciate all contributions that help improve the reproducibility and scientific rigour of this work.

---

**Vibrational Field Dynamics Institute**
