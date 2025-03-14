import os
import json

def load_api_key(key):
    """
    Load the OpenAI API key from a configuration file.
    
    Returns:
        str: The API key.
    """
    config_path = os.path.expanduser("~/config.json")  # Path to the config file
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
        return config[key]

# Load and set the API key
api_key = load_api_key(key)
