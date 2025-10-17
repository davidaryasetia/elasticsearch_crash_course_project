import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]

# Load environtment variable
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)


class Config:
    ES_HOST = os.getenv("ES_HOST")
    ES_USERNAME = os.getenv("ES_USERNAME")
    ES_PASSWORD = os.getenv("ES_PASSWORD")
