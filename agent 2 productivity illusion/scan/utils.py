"""Shared helpers: config load, dirs, console."""
import yaml
from pathlib import Path

def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)
    return path
