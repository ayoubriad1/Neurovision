# 🧠 Neurovision: Brain-Target Affinity Visualization

[![Python](https://img.shields.io/badge/Python-3.10--3.12-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)](#)

A powerful **Streamlit-based web application** for visualizing protein/pharmaceutical target binding affinity across 25 distinct brain regions. Enter binding scores in **kcal/mol** and watch them rendered as interactive heat maps on a realistic **3D brain surface** with multiple anatomical perspectives.

---

## 📋 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [Brain Regions](#-brain-regions)
- [Technical Details](#-technical-details)
- [Architecture](#-architecture)
- [Dependencies](#-dependencies)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🎯 Core Capabilities

- **3D Surface Rendering**  
  Realistic cortical surface visualization with gyri (ridges) and sulci (grooves) accurately represented. Heat maps follow the brain texture for anatomically accurate representation.

- **8 Anatomical Views**  
  - **Lateral (Left/Right)** — Outside surface of each hemisphere as viewed from the side
  - **Medial (Left/Right)** — Inner surface with the brain split down the middle
  - **Dorsal** — Bird's-eye view from above the head
  - **Ventral** — View from below, showing the brain's underside

- **3 Visualization Modes**
  - **3D Surface** (Default) — Paper-style layout matching neuroscience publications
  - **Glass Brain** — Transparent projection showing all regions simultaneously
  - **Stat Map (Slices)** — Anatomical cross-sections, ideal for subcortical structures

- **25 Brain Regions**  
  Comprehensive coverage from cortical areas to deep subcortical structures, all mapped to MNI152 standard coordinates:
  - Prefrontal regions (DLPFC, VMPFC, OFC)
  - Cingulate structures (ACC, PCC)
  - Temporal lobe regions
  - Limbic system (Hippocampus, Amygdala, Thalamus)
  - Basal ganglia (Striatum, Nucleus Accumbens)
  - Brainstem structures (Substantia Nigra, VTA, Raphe)
  - Cerebellum and more

- **kcal/mol Input Conversion**  
  Enter docking scores directly (e.g., `-7.8 kcal/mol`), automatically converted to visual intensity (0-100%) for intuitive interpretation.

- **Interactive Controls**  
  Streamlit-based sidebar with dropdown region selection, numerical input fields, and real-time visualization updates.

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10, 3.11, or 3.12** (3.13+ not yet supported by nilearn)
- **Git** (for version control)
- **Conda** or **pip** (for package management)

### Installation (2 minutes)

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/neurovision.git
cd neurovision

# Create a Python environment (Conda recommended)
conda create -n neurovision python=3.12 -y
conda activate neurovision

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

Your browser will automatically open to **http://localhost:8501**. If not, navigate there manually.

---

## 📦 Installation

### Option 1: Conda (Recommended)

Best for scientific Python work with pre-compiled binary packages.

```bash
# Create environment
conda create -n neurovision python=3.12 -y

# Activate environment
conda activate neurovision

# Install dependencies
pip install -r requirements.txt
```

### Option 2: venv (Virtual Environment)

Standard Python approach, works across all platforms.

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Verification

Check that all packages installed correctly:

```bash
python -c "import streamlit; import nilearn; import nibabel; print('✓ All packages installed successfully')"
```

---

## 🎮 Usage

### Step-by-Step Guide

1. **Launch the Application**
   ```bash
   streamlit run app.py
   ```

2. **Select a Brain Region**  
   Use the sidebar dropdown menu to choose from 25 brain regions.

3. **Enter Binding Affinity**  
   Input the docking score in **kcal/mol** (typically a negative number):
   - Example: `-7.8` (stronger binding)
   - Example: `-3.2` (weaker binding)

4. **Click "Add Region"**  
   The region-score pair is added to your visualization. Repeat for multiple regions.

5. **Choose View Mode**
   - **3D Surface** — Best for publication-quality figures
   - **Glass Brain** — Best for seeing all regions at once in 3D
   - **Stat Map (Slices)** — Best for subcortical structures (thalamus, hippocampus, etc.)

6. **Explore the Interactive Guide**  
   Expand "How to read the views" for detailed explanations of each panel.

---

## 🧬 Brain Regions

### Complete Region List with MNI Coordinates

| Region | Coordinates (x, y, z) | Anatomical Type |
|--------|----------------------|-----------------|
| **Striatum (Caudate)** | (12, 12, 8) | Basal Ganglia |
| **Striatum (Putamen)** | (28, 4, 2) | Basal Ganglia |
| **Nucleus Accumbens** | (10, 12, -8) | Basal Ganglia (Reward) |
| **Globus Pallidus** | (16, 2, -2) | Basal Ganglia |
| **Prefrontal Cortex (DLPFC)** | (-40, 32, 30) | Executive Function |
| **Prefrontal Cortex (VMPFC)** | (2, 46, -10) | Decision Making |
| **Orbitofrontal Cortex** | (-30, 28, -14) | Reward/Value |
| **Anterior Cingulate Cortex** | (0, 34, 18) | Emotion/Attention |
| **Posterior Cingulate Cortex** | (0, -50, 30) | Default Mode Network |
| **Hippocampus** | (-28, -22, -14) | Memory |
| **Amygdala** | (-24, -4, -18) | Emotion/Fear |
| **Thalamus** | (0, -12, 8) | Relay/Integration |
| **Hypothalamus** | (0, -4, -10) | Neuroendocrine |
| **Substantia Nigra** | (-10, -18, -12) | Dopamine |
| **Ventral Tegmental Area** | (0, -16, -14) | Reward/Dopamine |
| **Raphe Nuclei** | (0, -28, -24) | Serotonin |
| **Locus Coeruleus** | (-2, -36, -24) | Norepinephrine |
| **Insula** | (-36, 14, 2) | Interoception |
| **Cerebellum** | (0, -60, -30) | Motor Coordination |
| **Primary Motor Cortex** | (-38, -22, 56) | Motor Control |
| **Somatosensory Cortex** | (-42, -28, 54) | Touch/Proprioception |
| **Visual Cortex (V1)** | (4, -82, 4) | Vision |
| **Auditory Cortex** | (-54, -22, 8) | Hearing |
| **Temporal Pole** | (-38, 14, -30) | Memory/Social |
| **Parietal Cortex (SPL)** | (-26, -58, 52) | Spatial Attention |

---

## 🔬 Technical Details

### kcal/mol to Intensity Conversion

The binding affinity (in kcal/mol) is converted to a visualization intensity (0-100%) using the formula:

```
intensity = (|kcal/mol| - 1) / (15 - 1) × 100
```

**Interpretation:**
- **-1 kcal/mol** → 0% intensity (weakest binding, very faint)
- **-15 kcal/mol** → 100% intensity (strongest binding, brightest red)
- Values outside [-15, -1] are clamped to this range

**Example:**
```
Input:  -9.2 kcal/mol
Calculation: (9.2 - 1) / 14 × 100 = 58.6%
Visualization: Medium-intense orange-red color
```

### 3D Gaussian Blob Generation

For each brain region:

1. **MNI Coordinate Conversion** — Region's MNI coordinates are converted to voxel indices
2. **3D Gaussian Blob Creation** — A 3D Gaussian function is placed at the region's location with:
   - **Amplitude** proportional to binding intensity
   - **Spread (σ)** of 12mm for surface visualization (allows deep structures to appear on cortical surface)
3. **Volume Accumulation** — All regional blobs are summed into a single NIfTI volume
4. **Surface Projection** — The volume is projected onto the FreeSurfer fsaverage cortical surface

### MNI152 Space

All coordinates are in the **MNI152 standard brain template**, ensuring compatibility with neuroimaging literature and tools.

---

## 🏗️ Architecture

### Project Structure

```
neurovision/
│
├── app.py                      # Streamlit UI, kcal/mol conversion, user interface
├── brain_regions.py            # 25 brain regions + MNI coordinates dictionary
├── visualization.py            # NIfTI generation, 3D surface/glass/stat rendering
├── requirements.txt            # Python package dependencies
├── .gitignore                  # Git ignore rules
├── LICENSE                     # MIT License
├── CONTRIBUTING.md             # Contribution guidelines
└── README.md                   # This file
```

### Data Flow Diagram

```
User Input
    ↓
[app.py] — Streamlit UI, region selector, kcal/mol input
    ↓
[brain_regions.py] — Fetch MNI coordinates for selected region
    ↓
[visualization.py] — Create NIfTI activation volume
    ↓
[nilearn] — Project onto cortical surface
    ↓
[matplotlib] — Render 8 views (lateral, medial, dorsal, ventral)
    ↓
Browser Display — Interactive visualization
```

### Key Functions

**app.py:**
- `streamlit.run()` — Main application loop
- KCAL_MIN/MAX constants — Binding affinity range
- GUIDE_* strings — View explanations

**brain_regions.py:**
- `BRAIN_REGIONS` dict — Region names → MNI coordinates
- `get_region_names()` — Returns sorted list of region names
- `get_coordinates(name)` — Returns (x, y, z) for a region

**visualization.py:**
- `create_activation_volume()` — Generate NIfTI from regions + scores
- `_mni_to_voxel()` — Convert MNI coordinates to voxel space
- `plot_brain_surface()` — Render 8-view surface layout
- `plot_brain_glass()` — Render 4-view glass brain projection
- `plot_brain_stat()` — Render anatomical slices + cross-sections

---

## 📚 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **streamlit** | ≥1.30.0 | Web application framework, interactive UI |
| **nilearn** | ≥0.10.0 | Brain surface rendering, projections, stat maps |
| **matplotlib** | ≥3.7.0 | Figure rendering, image composition |
| **nibabel** | ≥5.0.0 | NIfTI image I/O (neuroimaging format) |
| **numpy** | ≥1.24.0 | Numerical computing, Gaussian blob generation |

**Note:** Install all at once with:
```bash
pip install -r requirements.txt
```

---

## 🌐 View Modes Explained

### 3D Surface Mode (Default)

**Best for:** Publication-quality figures, cortical focus

**Layout:**
```
┌──────────────────────────────────────┐
│ LEFT LATERAL  │ RIGHT LATERAL        │
│ (Left side)   │ (Right side)         │
├──────────────────────────────────────┤
│ FRONT VIEW    │ DORSAL (Top)         │
│ VENTRAL (Bottom) with COLORBAR       │
└──────────────────────────────────────┘
```

**Color Scale:** Gray (no activation) → Yellow (weak) → Orange → Red (strong)

### Glass Brain Mode

**Best for:** Seeing all regions simultaneously, understanding 3D distribution

**Views:**
- Left & Right Sagittal — Side-to-side projection
- Axial — Top-to-bottom projection
- Coronal — Front-to-back projection

These are **full-depth projections** (like X-rays), so deep structures are always visible.

### Stat Map Mode (Slices)

**Best for:** Inspecting subcortical structures, precise anatomical location

**Contains:**
- 6 axial slices — Horizontal cuts from bottom to top
- 3 orthogonal cross-sections — Sagittal, coronal, axial at peak activation location

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Code style guidelines
- How to report bugs
- How to submit pull requests
- Development setup

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes and test thoroughly
4. Commit: `git commit -am 'Add my feature'`
5. Push: `git push origin feature/my-feature`
6. Open a pull request

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for full details.

**Key points:**
- ✅ Free to use, modify, and distribute
- ✅ Can be used for commercial purposes
- ✅ Must include the license notice when distributed
- ❌ Comes with no warranty

---

## 🔗 References & Resources

### Neuroimaging Standards
- [MNI152 Template](https://www.mcgill.ca/brain-imaging/resources)
- [FreeSurfer Project](https://surfer.nmr.mgh.harvard.edu/)
- [Nilearn Documentation](https://nilearn.github.io/)

### Related Tools
- [Nibabel](https://nipy.org/nibabel/) — Neuroimaging I/O
- [FSL](https://fsl.fmrib.ox.ac.uk/) — FMRI Software Library
- [SPM](https://www.fil.ion.ucl.ac.uk/spm/) — Statistical Parametric Mapping

---

## 💬 Support & Questions

- **Issues:** Open a GitHub issue for bugs or feature requests
- **Discussions:** Use GitHub Discussions for questions and ideas
- **Email:** Contact the maintainers for specific inquiries

---

## 🎯 Roadmap

Future enhancements:
- [ ] Custom brain region definition
- [ ] Export to NIfTI files
- [ ] Batch processing for multiple compounds
- [ ] Integration with docking software output
- [ ] 3D interactive viewer (Three.js)
- [ ] Receptor mapping database
- [ ] Comparative analysis tools

---

## Acknowledgments

This project builds on decades of neuroimaging research and open-source tools:
- FreeSurfer for cortical surface templates
- Nilearn for visualization pipelines
- Streamlit for the web interface

---

**Last updated:** May 2026  
**Version:** 1.0.0  
**Status:** Active Development
