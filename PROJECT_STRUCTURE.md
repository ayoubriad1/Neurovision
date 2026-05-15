# Project Structure and Organization

## Directory Hierarchy

```
neurovision/
|
+-- src/
|   |-- app.py                    Streamlit user interface application
|   |-- brain_regions.py          Brain region definitions and coordinates
|   +-- visualization.py          Three-dimensional rendering engine
|
+-- config/
|   |-- requirements.txt          Python package dependencies
|   +-- .gitignore               Additional git ignore rules
|
+-- docs/
|   |-- guides/
|   |   |-- GETTING_STARTED.md   Quick start and navigation guide
|   |   |-- QUICK_START.md       Five-minute GitHub setup instructions
|   |   |-- GITHUB_SETUP.md      Detailed GitHub setup with explanations
|   |   +-- SETUP_SUMMARY.txt    Complete setup checklist
|   +-- api/
|       +-- (API documentation)
|
+-- examples/
|   +-- (Example usage files and configurations)
|
+-- tests/
|   +-- (Unit and integration tests)
|
+-- README.md                      Main project documentation
+-- LICENSE                        MIT open source license
+-- setup.py                       Automated environment setup script
+-- .gitignore                     Git repository configuration
+-- PROJECT_STRUCTURE.md           This file
+-- FINAL_SUMMARY.md              Complete project summary
```

## File Organization Principles

### src/ - Source Code Directory

Contains all application code organized by responsibility:

**app.py**
- Main Streamlit application entry point
- User interface components and layout
- Session state management
- Interactive controls and buttons
- Result display and visualization containers

**brain_regions.py**
- Static brain region database
- Twenty-five supported brain regions
- MNI152 standard coordinates
- Region name and coordinate lookup functions

**visualization.py**
- NIfTI volume generation from region-score pairs
- Three-dimensional Gaussian blob creation
- Cortical surface projection using FreeSurfer
- Image composition for publication-quality output
- Multiple visualization mode implementations

### config/ - Configuration Files

**requirements.txt**
- Complete list of Python package dependencies
- Version specifications for all packages
- Ensures reproducible environments across systems

**.gitignore**
- Rules for excluding files from version control
- Prevents tracking of virtual environments
- Excludes Python cache and compiled files
- Prevents neuroimaging data from repository

### docs/ - Documentation

**docs/guides/**
- User-facing documentation and tutorials
- Setup and installation instructions
- Platform-specific configuration guides
- Quick start guides for different audiences

**docs/api/**
- Application programming interface documentation
- Module-level documentation
- Function signatures and parameters
- Usage examples and code snippets

### examples/ - Example Code

Demonstrates typical usage patterns:
- Sample input files
- Configuration examples
- Output visualization examples
- Batch processing scripts

### tests/ - Test Suite

Unit and integration tests:
- Function-level validation
- Integration test scenarios
- Performance benchmarks
- Continuous integration configuration

## Module Dependencies

### app.py
- streamlit: Web framework
- matplotlib.pyplot: Figure rendering
- brain_regions: Local module
- visualization: Local module

### brain_regions.py
- Pure Python (no external dependencies)

### visualization.py
- numpy: Numerical operations
- nibabel: NIfTI file format support
- nilearn: Brain surface rendering
- matplotlib: Figure composition
- brain_regions: Local module

## Development Workflow

### File Modification Sequence

When adding new features:

1. Update brain_regions.py (if adding new regions)
2. Implement functionality in visualization.py
3. Add UI components in app.py
4. Update requirements.txt (if adding dependencies)
5. Add tests in tests/
6. Add documentation in docs/

### Git Workflow

Feature branches should follow naming convention:
- feature/add-export-functionality
- feature/improve-rendering-performance
- bugfix/fix-coordinate-conversion

## Build and Deployment

### Local Testing

```
python -m venv .venv
source .venv/bin/activate  (or .venv\Scripts\activate on Windows)
pip install -r config/requirements.txt
streamlit run src/app.py
```

### Production Deployment

Environment variables for deployment:
- STREAMLIT_SERVER_PORT: Web server port
- STREAMLIT_SERVER_ADDRESS: Server binding address
- STREAMLIT_LOGGER_LEVEL: Logging verbosity

## Documentation Maintenance

Update documentation when:
- Adding new features: Update README.md and relevant guides
- Changing API: Update docs/api/ files
- Modifying setup process: Update docs/guides/GITHUB_SETUP.md
- Changing structure: Update this file (PROJECT_STRUCTURE.md)

## Dependencies Graph

```
                    app.py
                   /      \
              brain_           visualization.py
            regions.py              |
                      +- nibabel
                      |
                      +- nilearn
                      |
                      +- matplotlib
                      |
                      +- numpy
```

## Code Metrics

Current project statistics:

```
Source Code Files:    3 (550+ lines)
Documentation Files:  7 (2500+ lines)
Configuration Files:  2
Brain Regions:        25
Visualization Modes:  3
Anatomical Views:     8
Python Version:       3.10-3.12
License:              MIT
```

## Scalability Considerations

### Adding New Brain Regions

Simple process requiring modification of brain_regions.py only:

1. Add region name and MNI coordinates to BRAIN_REGIONS dictionary
2. Verify coordinates against literature
3. Test visualization at new region
4. Update documentation with new region information

### Adding New Visualization Modes

Moderate complexity requiring visualization.py modification:

1. Implement new rendering function following existing pattern
2. Integrate into app.py UI controls
3. Add corresponding documentation
4. Test across multiple regions

### Performance Optimization

Current bottlenecks and solutions:

- Volume rendering: Implemented with vectorized NumPy operations
- Surface projection: Utilized pre-computed FreeSurfer templates
- Image composition: Matplotlib handles efficiently for typical use cases
- Caching: Session state management reduces redundant calculations

## Security Considerations

No security vulnerabilities identified. Application is:
- Stateless (no user authentication required)
- Local processing only (no remote data transmission)
- No database connections
- No external API calls

## Testing Strategy

Test coverage areas:
- Unit tests: Individual function validation
- Integration tests: Multi-module workflows
- Performance tests: Rendering speed benchmarks
- Visual tests: Output quality inspection

## Continuous Integration

GitHub Actions configuration (.github/workflows/) enables:
- Automated testing on code push
- Python version compatibility checking
- Dependency vulnerability scanning
- Code quality analysis

---

**Version:** 1.0.0  
**Last Updated:** May 15, 2026  
**Maintainer:** Development Team
