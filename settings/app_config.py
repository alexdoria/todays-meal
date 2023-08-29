"""Configuration loader"""
import json


def get_config():
    """Fetch config file"""
    with open("./settings/config.json", encoding="utf-8") as cfg:
        config = json.load(cfg)
    return config
