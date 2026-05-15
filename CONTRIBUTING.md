# Contributing

Contributions are welcome! Here's how to get started.

## Reporting Issues

- Open an issue on GitHub describing the bug or feature request.
- Include your Python version, OS, and any error messages.

## Development Setup

```bash
git clone https://github.com/YOUR_USERNAME/neuro-target-visualizer.git
cd neuro-target-visualizer
conda create -n brainviz-dev python=3.12 -y
conda activate brainviz-dev
pip install -r requirements.txt
```

## Making Changes

1. Fork the repository and create a feature branch.
2. Make your changes.
3. Test locally with `streamlit run app.py`.
4. Submit a pull request with a clear description of your changes.

## Adding New Brain Regions

To add a new region, edit `brain_regions.py`:

1. Find the MNI152 coordinates for your region (from a published atlas or resource like Neurosynth).
2. Add an entry to the `BRAIN_REGIONS` dictionary:
   ```python
   "Region Name": (x, y, z),
   ```
3. The region will automatically appear in the dropdown.

## Code Style

- Keep it simple. No unnecessary abstractions.
- Follow existing patterns in the codebase.
- Test both Glass Brain and Stat Map views after changes.
