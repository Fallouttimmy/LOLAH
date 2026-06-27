from core.logger import Logger
from config.settings import Settings

class Assistant:
    def __init__(self):
        self.settings = Settings()
        self.logger = Logger(level=self.settings.get("log_level", "INFO"))

    def start(self):
        self.logger.info("Assistant core initialized.")

    def process(self, text: str):
        self.logger.info(f"Received input: {text}")
        
        if "hello" in text.lower():
            return "Hello! I am Lolah."
        
        return "I am still learning."
