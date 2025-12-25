import tomllib
import os
from pathlib import Path
def load_config():
    try:
        config_path=Path("tools.toml")
    except:
        raise FileNotFoundError("tools.toml file not found")
    with open(config_path,"rb") as file:
        return tomllib.load(file)
    