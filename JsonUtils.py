import json


class JsonUtils:

    @classmethod
    def read_json(cls):
        # Read the JSON config file and returns it as a parsed dict
        with open('config.json') as config_file:
            config = json.load(config_file)
        return config
