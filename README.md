# NEUROVISION: Brain-Target Affinity Visualization

## Overview

Neurovision is a web-based application for visualizing pharmaceutical target binding affinity across 25 distinct brain regions. This tool converts binding scores measured in kcal/mol into interactive three-dimensional brain surface visualizations suitable for scientific analysis and publication.

**Current Version:** 1.0.0  
**License:** MIT  
**Python Support:** 3.10 - 3.12

---

## Features

### Core Capabilities

**Three-Dimensional Surface Rendering**
Realistic cortical surface visualization incorporating anatomical gyri (ridges) and sulci (grooves). Heat map overlays accurately follow brain topology for authentic anatomical representation.

**Comprehensive Anatomical Coverage**
Access to 25 distinct brain regions spanning cortical and subcortical structures:
- Prefrontal regions (DLPFC, VMPFC, OFC)
- Cingulate cortex (ACC, PCC)
- Limbic structures (Hippocampus, Amygdala, Thalamus)
- Basal ganglia (Striatum, Nucleus Accumbens, Globus Pallidus)
- Brainstem nuclei (VTA, Substantia Nigra, Raphe Nuclei, Locus Coeruleus)
- Sensory cortices (Visual, Auditory, Somatosensory)
- Additional regions (Insula, Cerebellum, Temporal Pole, Parietal Cortex)

**Multiple Visualization Modes**

   3D Surface Mode
   Lateral, medial, dorsal, and ventral views of brain surface
   Publication-quality rendering matching peer-reviewed neuroimaging literature

   Glass Brain Mode
   Transparent volumetric projections from four angles
   Simultaneous visualization of all regions in three-dimensional space
   Suitable for overview and comparative analysis

   Statistical Map Mode
   Anatomical cross-sections at regular intervals
   Orthogonal slices through peak activation regions
   Optimized for subcortical structure inspection

**Binding Affinity Input System**
Direct entry of docking scores in kcal/mol units. Automatic conversion to normalized intensity scale (0-100%) enables intuitive interpretation of binding strength across all regions.

---

## Technical Specifications

### System Requirements

**Python Environment**
- Python 3.10, 3.11, or 3.12 (required)
- Python 3.13+ not currently supported due to nilearn compatibility
- Virtual environment (Conda or venv) strongly recommended

**Hardware Specifications**
- Processor: Intel Core i5 equivalent or better
- Memory: 4 GB RAM minimum, 8 GB recommended
- Storage: 2 GB available disk space
- Display: 1920x1080 or higher resolution

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | >= 1.30.0 | Web application framework |
| nilearn | >= 0.10.0 | Neuroimaging visualization library |
| nibabel | >= 5.0.0 | NIfTI file format support |
| matplotlib | >= 3.7.0 | Figure composition and rendering |
| numpy | >= 1.24.0 | Numerical computing operations |

---

## Installation Guide

### Method 1: Using Conda (Recommended)

Conda provides pre-compiled scientific Python packages suitable for neuroimaging applications.

    Step 1: Create Environment
    conda create -n neurovision python=3.12 -y

    Step 2: Activate Environment
    conda activate neurovision

    Step 3: Install Dependencies
    pip install -r config/requirements.txt

    Step 4: Verify Installation
    python -c "import streamlit, nilearn, nibabel, numpy; print('Installation successful')"


### Method 2: Using Python Virtual Environment

Standard Python approach compatible with all operating systems.

    Step 1: Create Virtual Environment
    python -m venv .venv

    Step 2: Activate (Choose Your Operating System)
    
    Windows:
    .venv\Scripts\activate
    
    macOS/Linux:
    source .venv/bin/activate

    Step 3: Install Dependencies
    pip install -r config/requirements.txt

    Step 4: Verify Installation
    python -c "import streamlit, nilearn, nibabel, numpy; print('Installation successful')"


### Method 3: Automated Setup Script

Python script handles environment creation and dependency installation.

    python setup.py --method venv
    # or
    python setup.py --method conda


---

## Usage Instructions

### Launching the Application

After completing installation and activating your environment:

    streamlit run src/app.py

The application launches in your default web browser at http://localhost:8501

### Typical Workflow

**Step 1: Region Selection**
Choose a brain region from the dropdown selector in the left sidebar. Available regions sorted alphabetically from 25 supported structures.

**Step 2: Binding Affinity Input**
Enter binding affinity score in kcal/mol format. Values typically range from -1 (weakest binding) to -15 (strongest binding). Negative values indicate favorable binding thermodynamics.

Example values:
- -3.2 kcal/mol: weak binding (14% intensity)
- -7.8 kcal/mol: moderate binding (48% intensity)
- -12.5 kcal/mol: strong binding (82% intensity)

**Step 3: Region Addition**
Click "Add Region" button to incorporate region-binding pair into visualization. Repeat for additional regions to build complete binding profile.

**Step 4: Visualization Mode Selection**
Choose visualization approach from sidebar options:
- 3D Surface: best for publication figures
- Glass Brain: best for comprehensive overview
- Stat Map: best for subcortical analysis

**Step 5: Result Interpretation**
Expand "How to read the views" section for detailed guidance on interpreting each visualization panel. Color scale progresses from yellow (weak) through orange to red (strong binding).


---

## Brain Regions Database

All coordinates referenced to MNI152 standard brain template enabling compatibility with neuroimaging literature.


```
CORTICAL REGIONS

Frontal Lobe
  Prefrontal Cortex (DLPFC)       (-40,  32,  30)
  Prefrontal Cortex (VMPFC)       (  2,  46, -10)
  Orbitofrontal Cortex            (-30,  28, -14)
  Primary Motor Cortex            (-38, -22,  56)

Cingulate Cortex
  Anterior Cingulate Cortex       (  0,  34,  18)
  Posterior Cingulate Cortex      (  0, -50,  30)

Temporal Lobe
  Auditory Cortex                 (-54, -22,   8)
  Temporal Pole                   (-38,  14, -30)

Parietal and Occipital
  Somatosensory Cortex            (-42, -28,  54)
  Visual Cortex (V1)              (  4, -82,   4)
  Parietal Cortex (SPL)           (-26, -58,  52)

Insular Cortex
  Insula                          (-36,  14,   2)


SUBCORTICAL STRUCTURES

Basal Ganglia
  Striatum (Caudate)              ( 12,  12,   8)
  Striatum (Putamen)              ( 28,   4,   2)
  Nucleus Accumbens               ( 10,  12,  -8)
  Globus Pallidus                 ( 16,   2,  -2)

Limbic System
  Hippocampus                     (-28, -22, -14)
  Amygdala                        (-24,  -4, -18)
  Thalamus                        (  0, -12,   8)
  Hypothalamus                    (  0,  -4, -10)

Brainstem
  Substantia Nigra                (-10, -18, -12)
  Ventral Tegmental Area          (  0, -16, -14)
  Raphe Nuclei                    (  0, -28, -24)
  Locus Coeruleus                 ( -2, -36, -24)

Other Structures
  Cerebellum                      (  0, -60, -30)
```

---

## Data Processing Pipeline


```
                    USER INPUT
                        |
                        v
            ┌───────────────────────┐
            |  Region Selection     |
            |  Binding Score Entry  |
            └───────────┬───────────┘
                        |
                        v
            ┌───────────────────────┐
            | brain_regions.py      |
            | Coordinate Lookup     |
            | MNI Coordinates       |
            └───────────┬───────────┘
                        |
                        v
            ┌───────────────────────┐
            | visualization.py      |
            | Volume Generation     |
            | Gaussian Blob Creation|
            | Coordinate Conversion |
            └───────────┬───────────┘
                        |
                        v
            ┌───────────────────────┐
            | Intensity Calculation |
            | (kcal/mol to 0-100%)  |
            | Accumulation          |
            └───────────┬───────────┘
                        |
                        v
            ┌───────────────────────┐
            | Surface Projection    |
            | FreeSurfer fsaverage  |
            | NIfTI Processing      |
            └───────────┬───────────┘
                        |
                        v
            ┌───────────────────────┐
            | Matplotlib Rendering  |
            | View Composition      |
            | Color Mapping         |
            └───────────┬───────────┘
                        |
                        v
            ┌───────────────────────┐
            |   BROWSER DISPLAY     |
            | Interactive Streamlit |
            │      Interface        |
            └───────────────────────┘
```

---

## Binding Affinity Conversion Formula

The application converts binding affinities from kcal/mol to visual intensity using the following scaling:

```
intensity (%) = (|kcal/mol| - 1) / (15 - 1) * 100

Defined Range: -1 to -15 kcal/mol
Output Range:  0 to 100%
```

**Conversion Examples:**

| Input (kcal/mol) | Calculation | Output (%) | Visualization |
|------------------|-------------|-----------|---|
| -1.0 | (1 - 1) / 14 × 100 | 0% | Gray (no activation) |
| -3.0 | (3 - 1) / 14 × 100 | 14% | Light yellow |
| -7.0 | (7 - 1) / 14 × 100 | 43% | Yellow-orange |
| -9.2 | (9.2 - 1) / 14 × 100 | 59% | Orange |
| -12.5 | (12.5 - 1) / 14 × 100 | 82% | Red-orange |
| -15.0 | (15 - 1) / 14 × 100 | 100% | Dark red |

Values outside the range [-15, -1] are automatically clamped to nearest boundary.

---

## Project Structure

```
neurovision/
|
+-- src/
|   |-- app.py                  Main Streamlit application
|   |-- brain_regions.py        Brain region definitions
|   +-- visualization.py        Rendering engine
|
+-- config/
|   +-- requirements.txt        Python dependencies
|
+-- docs/
|   |-- guides/
|   |   |-- GETTING_STARTED.md
|   |   |-- QUICK_START.md
|   |   |-- GITHUB_SETUP.md
|   |   +-- SETUP_SUMMARY.txt
|   |-- api/
|   +-- CONTRIBUTING.md
|
+-- examples/
|   +-- (example usage files)
|
+-- tests/
|   +-- (test files)
|
+-- README.md
+-- LICENSE
+-- setup.py
+-- .gitignore
+-- PROJECT_STRUCTURE.md
+-- FINAL_SUMMARY.md
```

---

## Module Documentation

### src/app.py

Main Streamlit application handling user interface and interaction. Manages:
- Sidebar region selection dropdown
- Binding affinity numerical input
- Region addition to active visualization
- View mode selection and switching
- Interactive guidance and explanations
- Session state management

Key Constants:
- KCAL_MIN: -15.0 (strongest binding reference)
- KCAL_MAX: -1.0 (weakest binding reference)
- SURFACE_SIGMA: 12.0 mm (Gaussian spread for 3D surface projection)
- DEFAULT_SIGMA: 6.0 mm (Gaussian spread for other modes)

### src/brain_regions.py

Static database containing 25 brain regions and their MNI152 coordinates.

Structure:
```python
BRAIN_REGIONS = {
    "Region Name": (x, y, z),  # MNI coordinates
    ...
}
```

Functions:
- get_region_names(): Returns sorted list of all region names
- get_coordinates(name): Returns (x, y, z) tuple for named region

### src/visualization.py

Neuroimaging visualization engine utilizing nilearn and matplotlib.

Core Functions:

create_activation_volume(regions_and_scores, sigma)
- Generates three-dimensional NIfTI volume from region-score pairs
- Creates Gaussian blobs at MNI coordinates
- Applies intensity scaling
- Returns nibabel.Nifti1Image object

plot_brain_surface(nifti_img)
- Projects volume onto cortical surface
- Generates eight anatomical views
- Composites into publication-quality figure
- Returns matplotlib.figure.Figure

plot_brain_glass(nifti_img)
- Creates transparent volumetric projections
- Four viewing angles (sagittal left, axial, sagittal right, coronal)
- Suitable for comprehensive region visualization
- Returns matplotlib.figure.Figure

plot_brain_stat(nifti_img)
- Generates anatomical cross-sections
- Six axial slices plus orthogonal cross-sections
- Optimized for subcortical structure inspection
- Returns matplotlib.figure.Figure

---

## Visualization Guidelines

### Three-Dimensional Surface Mode

Most suitable for publication figures in neuroscience journals. Displays brain cortical surface from eight distinct perspectives providing complete spatial understanding.

Color Scale Interpretation:
- Gray: No activation (below 1% intensity threshold)
- Yellow: Weak to moderate binding (10-40% intensity)
- Orange: Moderate to strong binding (40-70% intensity)
- Red: Strong binding (70-100% intensity)

### Glass Brain Mode

Enables simultaneous visualization of all regions in three-dimensional volumetric space. Each panel represents full-depth projection eliminating occlusion of deep structures.

Four Viewing Angles:
- Left Sagittal: Left-to-right depth projection
- Axial: Superior-to-inferior depth projection
- Right Sagittal: Right-to-left depth projection
- Coronal: Anterior-to-posterior depth projection

### Statistical Map Mode

Cross-sectional display with six horizontal slices at regular intervals plus three orthogonal slices through peak activation region. Particularly useful for analyzing subcortical structures (thalamus, hippocampus, amygdala, basal ganglia).

---

## Technical Architecture

### Coordinate System

All brain coordinates reference MNI152 standard template (Montreal Neurological Institute 152-subject average). This standardized space enables:
- Compatibility with peer-reviewed neuroimaging literature
- Integration with neuroimaging databases
- Reproducibility across studies
- Cross-validation with published atlases

### Volume Processing

Three-dimensional Gaussian function placed at each region's MNI coordinates:

```
gaussian(x,y,z) = amplitude * exp(-(d² / (2σ²)))

where:
  d = distance from region center
  σ = spread parameter (12mm for surface, 6mm for other modes)
  amplitude = binding intensity (0-100%)
```

Multiple Gaussian blobs accumulate in single three-dimensional volume enabling composite visualization of multiple regions.

### Surface Rendering

FreeSurfer fsaverage cortical surface template provides realistic anatomical geometry. Volume projection maps three-dimensional NIfTI activation onto surface mesh enabling anatomically accurate visualization of both cortical and subcortical structures.

---

## Troubleshooting Guide

### Common Issues

**Issue: Application fails to launch**
```
Error: ModuleNotFoundError: No module named 'streamlit'
```
Solution: Verify all dependencies installed via requirements.txt. Reactivate environment.

**Issue: Blank visualization or missing regions**
```
Warning: Region coordinates out of bounds
```
Solution: Verify binding affinity values in valid range (-15 to -1 kcal/mol). Values outside range are automatically clamped.

**Issue: Slow rendering performance**
```
Observation: Visualization takes >10 seconds to render
```
Solution: Reduce number of displayed regions. Close other applications. Consider upgrading to 8GB RAM minimum.

**Issue: FreeSurfer surface data missing**
```
Error: Cannot find fsaverage template
```
Solution: Nilearn automatically downloads required data on first run. Ensure internet connectivity and 1GB free disk space.

---

## Contributing

Contributions welcome. Please refer to CONTRIBUTING.md for guidelines.

Development Environment Setup:
1. Clone repository
2. Create feature branch
3. Install development dependencies
4. Make changes with clear commit messages
5. Submit pull request for review

---

## License

This project is licensed under the MIT License. See LICENSE file for complete terms.

You are free to:
- Use commercially and privately
- Modify the source code
- Distribute copies

You must:
- Include the license notice in distributions
- Preserve copyright attribution

---

## References

### Primary Literature
The application architecture follows neuroimaging visualization best practices from:
- Yachou et al. (2025). [Original paper citation format]
- FreeSurfer: cortical surface analysis methods

### Key Resources
- MNI152 Template: Montreal Neurological Institute Brain Imaging Center
- FreeSurfer Project: https://surfer.nmr.mgh.harvard.edu/
- Nilearn Documentation: https://nilearn.github.io/
- Nibabel: https://nipy.org/nibabel/

---

## Support

For questions, issues, or suggestions:
1. Check documentation in docs/ folder
2. Review troubleshooting section above
3. Open issue on GitHub repository
4. Contact development team

---

## Citation

If using Neurovision in published research, please cite:

```
Neurovision: Brain-Target Affinity Visualization Tool
Version 1.0.0
https://github.com/ayoubriad1/neurovision
```

---

## Changelog

### Version 1.0.0 (May 2026)
- Initial public release
- 25 brain regions support
- Three visualization modes
- Streamlit web interface
- Comprehensive documentation

---

**Last Updated:** May 15, 2026  
**Maintained by:** Development Team  
**Status:** Active Development
