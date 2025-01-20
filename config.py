import os
from dotenv import load_dotenv

load_dotenv()

TASE_API_KEY = os.getenv("TASE_API_KEY")
MSEDGEDRIVER_PATH = os.getenv("MSEDGEDRIVER_PATH")

# Constants for paths, folders and file names
#---------------------------------------------------------------------------
CONFIG_FILE = 'config.py'
JSON_OUTPUT_FILE = 'api_output.json'
PY_OUTPUT_FILE = 'api_output.py'
PUBLIC_DIR_NAME = 'public_companies'
DATA_DIR_NAME = 'data'
COMPANIES_OUTPUT_DIR_NAME = 'companies_api_output'

# Function to get the project root directory
def get_project_root():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while current_dir != os.path.dirname(current_dir):
        if os.path.exists(os.path.join(current_dir, CONFIG_FILE)):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return None

BASE_DIR = get_project_root()
if BASE_DIR is None:
    raise RuntimeError("Project root not found.")

# Determine the base directory (project-root) based on this file's location
PUBLIC_PATH = os.path.join(BASE_DIR, PUBLIC_DIR_NAME )
DATA_PATH = os.path.join(PUBLIC_PATH, DATA_DIR_NAME )

# Construct the relative path to the 'output' folder
COMPANIES_OUTPUT_PATH = os.path.join(DATA_PATH, COMPANIES_OUTPUT_DIR_NAME)


