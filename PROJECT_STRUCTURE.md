# 📁 Neurovision Project Structure

Complete guide to the Neurovision repository organization.

---

## Directory Layout

```
neurovision/
│
├── 📖 README.md                     # Main project documentation
├── ⚖️  LICENSE                      # MIT License
├── 🔧 .gitignore                    # Git configuration
├── 🐍 setup.py                      # Automated setup script
│
├── 📁 src/                          # SOURCE CODE
│   ├── 🐍 app.py                    # Streamlit UI application
│   ├── 🐍 brain_regions.py          # Brain region definitions (25 regions)
│   ├── 🐍 visualization.py          # 3D rendering engine
│   ├── 📋 requirements.txt          # Python dependencies
│   └── 🔧 .gitignore               # Additional git ignores
│
└── 📁 docs/                         # DOCUMENTATION
    ├── 📖 00_START_HERE.md          # Navigation guide
    ├── 📖 QUICK_START.md            # 5-minute setup
    ├── 📖 GITHUB_SETUP_GUIDE.md     # Complete GitHub guide
    ├── 📖 CONTRIBUTING.md           # Contribution guidelines
    └── 📝 SETUP_SUMMARY.txt         # Full summary
```

---

## File Descriptions

### Root Level

| File | Purpose | Size |
|------|---------|------|
| **README.md** | Complete project documentation, features, usage, references | 14 KB |
| **LICENSE** | MIT License (open source) | 1.1 KB |
| **.gitignore** | Ignore cache, virtual envs, IDE files, notebooks | 1.5 KB |
| **setup.py** | Automated setup script (Conda or venv) | 4 KB |
| **PROJECT_STRUCTURE.md** | This file - directory organization | 3 KB |

### src/ — Source Code

| File | Purpose | Size | Lines |
|------|---------|------|-------|
| **app.py** | Main Streamlit application, UI, user interaction | 7.0 KB | 200+ |
| **brain_regions.py** | Brain region database (25 regions + coordinates) | 1.2 KB | 36 |
| **visualization.py** | 3D rendering, NIfTI generation, surface projection | 11 KB | 350+ |
| **requirements.txt** | Python package dependencies | 81 B | 5 |
| **.gitignore** | Additional ignores for source directory | - | - |

### docs/ — Documentation

| File | Purpose | Size | Audience |
|------|---------|------|----------|
| **00_START_HERE.md** | Navigation guide, what each doc contains | 2.8 KB | Everyone |
| **QUICK_START.md** | 5-minute GitHub setup with commands | 2.6 KB | Busy developers |
| **GITHUB_SETUP_GUIDE.md** | Detailed GitHub setup with explanations | 13 KB | Learning developers |
| **CONTRIBUTING.md** | How to contribute to the project | 1.2 KB | Contributors |
| **SETUP_SUMMARY.txt** | Complete setup summary & checklist | 12 KB | Reference |

---

## Module Dependencies

### src/app.py
```
├── streamlit          # Web UI framework
├── matplotlib.pyplot  # Figure rendering
├── brain_regions      # LOCAL: brain region definitions
└── visualization      # LOCAL: rendering functions
```

### src/brain_regions.py
```
(No external dependencies - pure Python dict)
```

### src/visualization.py
```
├── numpy              # Numerical computing
├── nibabel            # NIfTI file format
├── nilearn            # Brain surface rendering
├── matplotlib         # Figure composition
├── scipy (via nilearn)
└── brain_regions      # LOCAL: coordinate lookup
```

---

## Code Flow

```
User Opens App
    ↓
Streamlit Launches (app.py)
    ├── Import brain_regions
    ├── Import visualization functions
    └── Create Streamlit interface
        ↓
    User selects region + binding score
        ↓
    brain_regions.py: Get MNI coordinates
        ↓
    visualization.py: Create NIfTI volume
        ├── Generate 3D Gaussian blob
        ├── Place at MNI coordinates
        ├── Accumulate into volume
        └── Project onto cortical surface
        ↓
    matplotlib: Compose figures (8 views)
        ↓
    Display in browser
```

---

## Setup Variants

### Automatic Setup (Recommended)
```bash
# Using conda
python setup.py --method conda

# Using venv
python setup.py --method venv
```

### Manual Setup (Conda)
```bash
conda create -n neurovision python=3.12 -y
conda activate neurovision
pip install -r src/requirements.txt
streamlit run src/app.py
```

### Manual Setup (venv)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r src/requirements.txt
streamlit run src/app.py
```

---

## Key Design Decisions

### 1. **src/ for Source Code**
- Professional Python structure
- Keeps codebase organized
- Easy to package later (`pip install neurovision`)

### 2. **docs/ for Documentation**
- Separate from code
- Multiple docs for different audiences
- Easy to maintain versioned docs

### 3. **Root README.md**
- GitHub displays automatically
- Contains project overview
- Links to deeper docs

### 4. **setup.py**
- Automated environment setup
- Handles Conda and venv
- Verifies dependencies

### 5. **Comprehensive .gitignore**
- Excludes virtual environments
- Excludes IDE files
- Excludes neuroimaging data
- Excludes cache files

---

## File Sizes

```
Total project: ~65 KB
├── Source code (src/): ~20 KB
│   ├── app.py: 7.0 KB
│   ├── visualization.py: 11 KB
│   ├── brain_regions.py: 1.2 KB
│   └── requirements.txt: 81 B
│
├── Documentation (docs/): ~32 KB
│   ├── GITHUB_SETUP_GUIDE.md: 13 KB
│   ├── README.md: 14 KB
│   ├── SETUP_SUMMARY.txt: 12 KB
│   ├── QUICK_START.md: 2.6 KB
│   └── 00_START_HERE.md: 2.8 KB
│
└── Configuration: ~3 KB
    ├── LICENSE: 1.1 KB
    ├── .gitignore: 1.5 KB
    └── setup.py: 4 KB
```

---

## Adding New Features

### Add a new brain region:
1. Edit `src/brain_regions.py`
2. Add region name → MNI coordinates tuple

### Add visualization mode:
1. Add function to `src/visualization.py`
2. Import in `src/app.py`
3. Add UI option in sidebar

### Update documentation:
1. Edit files in `docs/`
2. Or edit `README.md`
3. Commit and push

---

## Git Workflow

```
1. Clone repo
   git clone https://github.com/YOUR_USERNAME/neurovision.git

2. Create feature branch
   git checkout -b feature/my-feature

3. Edit files (src/ or docs/)

4. Commit changes
   git add .
   git commit -m "Add my feature"

5. Push to GitHub
   git push origin feature/my-feature

6. Create Pull Request on GitHub
```

---

## Development Environment

Recommended tools:

| Tool | Purpose | Optional |
|------|---------|----------|
| VS Code / PyCharm | Code editor | ❌ Required |
| Miniconda | Package manager | ✅ Use pip if not available |
| Git | Version control | ❌ Required |
| Streamlit | Web framework | ❌ Required |

---

## Testing & Quality

### Before pushing to GitHub:
```bash
# Test imports
python -c "import src.app; import src.brain_regions; import src.visualization"

# Check syntax
python -m py_compile src/*.py

# Run the app locally
streamlit run src/app.py
```

---

## Deployment

### GitHub Pages (future)
1. Enable in Settings → Pages
2. Deploy docs to `gh-pages` branch

### Heroku (future)
1. Add `Procfile`
2. Add `heroku.yml`
3. Connect GitHub to Heroku

### Docker (future)
1. Create `Dockerfile`
2. Create `.dockerignore`
3. Push to Docker Hub

---

## Version Control Strategy

```
main branch
    ↑
    └── feature branches
        ├── feature/add-exports
        ├── feature/dark-mode
        └── feature/batch-processing
```

Each feature:
1. Branch off `main`
2. Develop in isolation
3. Pull Request for review
4. Merge back to `main`

---

## Documentation Maintenance

Update when:
- Adding features → Update README
- Changing setup → Update QUICK_START
- GitHub changes → Update GITHUB_SETUP_GUIDE
- Project-wide changes → Update PROJECT_STRUCTURE

---

## License & Attribution

This project uses:
- **Streamlit** (MIT License)
- **Nilearn** (BSD License)
- **Nibabel** (MIT License)
- **Matplotlib** (PSF License)
- **NumPy** (BSD License)

See LICENSE file and each package's docs for details.

---

## Quick Reference

```bash
# Setup
python setup.py --method venv

# Run
streamlit run src/app.py

# Test
python -m py_compile src/*.py

# Push to GitHub
git add .
git commit -m "Your message"
git push

# View logs
git log --oneline -5
```

---

**Last updated:** May 2026  
**Maintained by:** [Your Name]  
**Version:** 1.0.0
