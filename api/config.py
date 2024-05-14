import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        # flask app config
        self.DEBUG = os.getenv("DEBUG", False)

        # custom config
        self.HOST = os.getenv("HOST", "0.0.0.0")
        self.PORT = os.getenv("PORT", 5000)
