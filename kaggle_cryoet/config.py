"""
This module handles config loading.
"""
# %%
import os
import tomllib

def load_config(config_path: os.PathLike) -> dict:
    with open(config_path, "rb") as f:
        config = tomllib.load(f)
    return config

# %%
config = load_config("../config.toml")

# %%
