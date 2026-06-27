from core.logger import Logger
from config.settings import Settings

class Startup:
    def __init__(self):
        self.settings = Settings()
        self.logger = Logger(level=self.settings.get("log_level", "INFO"))

    def boot(self):
        self.logger.info("LOLAH starting up...")
        self.logger.info(f"Assistant Name: {self.settings.get('assistant_name')}")
        self.logger.info("Loading modules...")
        self.logger.info("Startup complete.")
