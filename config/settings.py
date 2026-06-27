import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

DEFAULT_CONFIG = {
    "assistant_name": "Lolah",
    "wake_word": "lolah",
    "language": "en",
    "offline_mode": True,
    "log_level": "INFO"
}

class Settings:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "w") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
            return DEFAULT_CONFIG

        with open(CONFIG_PATH, "r") as f:
            return json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        with open(CONFIG_PATH, "w") as f:
            json.dump(self.config, f, indent=4)
