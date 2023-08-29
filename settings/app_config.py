"""Configuration loader"""
import json


def get_config():
    """Fetch config file"""
    try:
        with open("./settings/config.json", encoding="utf-8") as cfg:
            config = json.load(cfg)
    except FileNotFoundError:
        print("Configuration file was not found, please type your API credentials")
        key = input("Type your API KEY: ")
        host = input("Enter host url: ")
        config = {
            "rapidapi": {
                "key": key,
                "host": host
            }
        }
    return config
