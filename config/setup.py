#!/usr/bin/env python3
"""
Neurovision Setup Script

Helps install Neurovision with proper dependency management.
Supports both Conda and pip virtual environments.

Usage:
    python setup.py --method conda
    python setup.py --method venv
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


class NeuroVisionSetup:
    def __init__(self, method="venv"):
        self.method = method
        self.project_dir = Path(__file__).parent
        self.src_dir = self.project_dir / "src"
        self.requirements_file = self.src_dir / "requirements.txt"

    def check_python_version(self):
        """Verify Python version is 3.10+"""
        version = sys.version_info
        if version.major < 3 or (version.major == 3 and version.minor < 10):
            print(f"❌ Python 3.10+ required. You have {version.major}.{version.minor}")
            sys.exit(1)
        print(f"✓ Python {version.major}.{version.minor} detected")

    def setup_conda(self):
        """Setup using Conda (recommended for scientific Python)"""
        print("\n📦 Setting up with Conda...")
        print("=" * 60)

        env_name = "neurovision"

        # Create conda environment
        print(f"Creating conda environment: {env_name}")
        subprocess.run([
            "conda", "create", "-n", env_name,
            "python=3.12", "-y"
        ], check=True)

        # Install requirements
        print("Installing dependencies...")
        subprocess.run([
            "conda", "run", "-n", env_name,
            "pip", "install", "-r", str(self.requirements_file)
        ], check=True)

        print("\n✅ Setup complete!")
        print(f"\nTo activate the environment:")
        print(f"   conda activate {env_name}")
        print(f"\nTo run Neurovision:")
        print(f"   streamlit run {self.src_dir / 'app.py'}")

    def setup_venv(self):
        """Setup using venv (standard Python)"""
        print("\n🐍 Setting up with venv...")
        print("=" * 60)

        venv_dir = self.project_dir / ".venv"

        # Create virtual environment
        print(f"Creating virtual environment: {venv_dir}")
        subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)

        # Get pip from venv
        if sys.platform == "win32":
            pip = venv_dir / "Scripts" / "pip.exe"
            activate = venv_dir / "Scripts" / "activate.bat"
            activate_cmd = str(activate)
        else:
            pip = venv_dir / "bin" / "pip"
            activate = venv_dir / "bin" / "activate"
            activate_cmd = f"source {activate}"

        # Install requirements
        print("Installing dependencies...")
        subprocess.run([str(pip), "install", "-r", str(self.requirements_file)], check=True)

        print("\n✅ Setup complete!")
        print(f"\nTo activate the environment:")
        print(f"   {activate_cmd}")
        print(f"\nTo run Neurovision:")
        print(f"   streamlit run {self.src_dir / 'app.py'}")

    def verify_installation(self):
        """Verify all dependencies installed correctly"""
        print("\n🔍 Verifying installation...")
        try:
            import streamlit
            import nilearn
            import nibabel
            import matplotlib
            import numpy
            print("✓ streamlit")
            print("✓ nilearn")
            print("✓ nibabel")
            print("✓ matplotlib")
            print("✓ numpy")
            print("\n✅ All dependencies verified!")
            return True
        except ImportError as e:
            print(f"❌ Missing dependency: {e}")
            return False

    def run(self):
        """Execute setup process"""
        print("=" * 60)
        print("  🧠 NEUROVISION SETUP")
        print("=" * 60)

        self.check_python_version()

        if self.method == "conda":
            self.setup_conda()
        elif self.method == "venv":
            self.setup_venv()
        else:
            print(f"❌ Unknown method: {self.method}")
            sys.exit(1)

        self.verify_installation()


def main():
    parser = argparse.ArgumentParser(
        description="Neurovision setup helper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python setup.py --method conda     # Use Conda (recommended)
  python setup.py --method venv      # Use venv (standard Python)
        """
    )

    parser.add_argument(
        "--method",
        choices=["conda", "venv"],
        default="venv",
        help="Setup method (default: venv)"
    )

    args = parser.parse_args()

    setup = NeuroVisionSetup(method=args.method)
    setup.run()


if __name__ == "__main__":
    main()
