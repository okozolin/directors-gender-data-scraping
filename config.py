import os
from dotenv import load_dotenv

load_dotenv()

TASE_API_KEY = os.getenv("TASE_API_KEY")
MSEDGEDRIVER_PATH = os.getenv("MSEDGEDRIVER_PATH")