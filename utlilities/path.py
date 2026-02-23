"""
Path for files
"""

from pathlib import Path

PROJECT_PATH = Path(__file__).parent.parent
CONFIGFILE_PATH = PROJECT_PATH.joinpath('config')
