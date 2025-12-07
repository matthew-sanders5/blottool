# BlotTool
*A reproducible, command-line toolkit for western blot densitometry.*

**Author:** Matthew T. Sanders  
**ORCID:** https://orcid.org/0009-0006-6419-7799  
**License:** MIT  

---

## Overview

**BlotTool** is a lightweight, open-source, CLI-based tool for western blot densitometry.  
It performs reproducible band quantification using user-defined rectangular ROIs and provides:

- FIJI-equivalent per-band intensities  
- Automated background subtraction  
- Deterministic reproducible outputs  
- Scriptable, GUI-free workflows  
- Overlay images for documentation  
- Validation against FIJI (included)

The tool is designed as a modern replacement for manual, error-prone clicking in FIJI/ImageJ, especially for labs that need batch processing, pipeline integration, or fully transparent quantification.

---

## Installation

```bash
git clone https://github.com/matthew-sanders5/blottool.git
cd blottool
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

Basic command:
```
blottool \
  --image example/example.png \
  --rois example/rois.csv \
  --out results.csv \
  --overlay overlay.png
```
This produces:
 - results.csv — intensities + background-corrected values
 - overlay.png — ROIs drawn on the image

## ROI Format

BlotTool reads ROI definitions from a CSV file:
```
label,x,y,width,height
lane1,15,152,90,40
lane2,110,165,90,40
lane3,210,165,90,40
...
```
Coordinates follow FIJI’s rectangle-tool convention (top-left anchored).

## Output Format

results.csv includes:
 - label
 - raw integrated density
 - raw mean gray
 - background mean
 - background integrated density
 - background-corrected integrated density
 - background-corrected mean gray

## Validation

BlotTool includes a FIJI comparison script:
```
python example/validate.py
```
Sample output:
```
=== FIJI vs blottool (band ROIs) ===
Max abs diff (mean gray): 0.00039
Max abs diff (IntDen):    0.0

Validation PASSED: blottool reproduces FIJI to <0.001 gray units.
```
All validation materials (raw blot, ROI CSV, FIJI tables) are included in example/.

## Features

 - Command-line interface (CLI)
 - FIJI-equivalent measurements
 - Automated background substraction
 - Deterministic reproducibility
 - Overlay image generation
 - Modular Python API
 - Comprehensive pytest suite
 - Packaged via pyproject.toml
 - Completely open-source and lightweight

## Why BlotTool?

Why BlotTool?

Western blot quantification is often performed in FIJI using manual clicking, leading to:

 - inconsistent ROI placement
 - undocumented background choices
 - limited reproducibility
 - difficulty scaling across experiments

BlotTool solves this by providing a simple, fully scriptable workflow that ensures repeatable measurements across experiments, users, labs, and machines.

## Citation

If you use BlotTool in published research, please cite:

Sanders MT. (2025). BlotTool: A reproducible command-line toolkit for western blot densitometry.

DOI will be added upon acceptance.

## License

Released under the MIT license. See LICENSE for details.
