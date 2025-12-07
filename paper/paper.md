---
title: "BlotTool: A reproducible command-line toolkit for western blot densitometry"
tags:
  - Python
  - biology
  - image analysis
  - western blot
  - reproducibility
  - densitometry
authors:
  - name: Matthew T. Sanders
    orcid: 0009-0006-6419-7799
    affiliation: 1
affiliations:
  - name: University of Kentucky, College of Agriculture, Food and Environment, Lexington, KY, USA
    index: 1
date: 7 December 2025
bibliography: paper.bib
---

# Summary

Western blot densitometry remains a bottleneck in many wet-lab workflows due to the reliance on GUI-driven tools such as FIJI/ImageJ. Manual ROI positioning, measurement, and background subtraction reduce reproducibility and complicate batch processing. **BlotTool** is a lightweight, open-source, command-line toolkit that provides a transparent, fully reproducible workflow for extracting band intensities from blot images using user-defined rectangular ROIs.

# Statement of Need

FIJI is widely used in biology labs but provides limited support for scripting, automation, and reproducibility. Densitometry is typically performed through manual clicking with inconsistent background correction and limited documentation of measurement parameters. BlotTool addresses these limitations by offering:

- a deterministic command-line interface,
- automated background subtraction,
- explicit ROI definitions in CSV,
- version-controlled processing,
- and reproducible validation against FIJI.

This enables batch-processing of blots, integration into larger analysis pipelines, and fully transparent quantification suitable for publication and reproducible research.

# Functionality

BlotTool accepts a blot image (PNG/TIF) and a CSV file of ROI definitions (`label, x, y, width, height`). It computes:

- band integrated density (sum of pixel values)
- mean gray value
- background ROI statistics
- background-corrected integrated density

An overlay image with ROIs drawn is generated for documentation. The tool includes a Python API and CLI. The codebase includes modular components (`io`, `measure`, `visualize`, `cli`) and a complete pytest suite (`tests/test_basic.py`, `tests/test_cli.py`, `tests/test_measure.py`).

# Validation

To ensure correctness, BlotTool was validated against FIJI. Using a standard blot with six lanes and corresponding background regions (Yikrazuul, 2007), BlotTool reproduced FIJI’s reported mean gray values and integrated density measurements to within **< 0.001 gray units** on a 0–255 scale and with **identical integrated density values**.

All validation datasets and scripts (`example/validate.py`) are included in the repository.

A representative ROI overlay is shown in \autoref{fig:Figure1}.

![Overlay image produced BlotTol using validation example blot.\{fig:Figure1}](overlay.png)

# Acknowledgements

The author thanks the developers of FIJI/ImageJ for establishing widely used measurement conventions that enable cross-tool validation.

# References
