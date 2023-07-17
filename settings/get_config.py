import json 


def get_config():
    with open("./settings/config.json") as cfg:
        config = json.load(cfg)
    return config