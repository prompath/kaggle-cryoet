"""
This module handles config loading.
"""

import json
import os
from pathlib import Path
import tomllib


def load_configs(config_dir: os.PathLike = "../configs") -> dict:
    config_dir = Path(config_dir).resolve()
    # Load project config
    with open(config_dir / "config.toml", "rb") as f:
        config = tomllib.load(f)
    # Load copick config
    with open(config_dir / "copick.json", "rb") as f:
        copick_json = json.load(f)
    config["COPICK"] = copick_json
    return config
