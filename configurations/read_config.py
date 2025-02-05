import json
import os


class ConfigReader:
    current_dir = os.getcwd()
    relative_path = os.path.join(current_dir, 'configurations', 'config.json')
    with open(relative_path, 'r') as file:
        config = json.load(file)

    @staticmethod
    def get_params(key):
        return ConfigReader.config.get(key)
