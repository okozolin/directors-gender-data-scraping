import os

from config import COMPANIES_OUTPUT_PATH, JSON_OUTPUT_FILE, PY_OUTPUT_FILE
from public_companies.helpers.file_handler import store_json_data, store_dict_data
from public_companies.tase_api import TASE


def save_to_file(tase_dict):
    # Ensure the output directory exists
    os.makedirs(COMPANIES_OUTPUT_PATH, exist_ok=True)

    # Define the file path for the file to be saved
    json_file_path = os.path.join(COMPANIES_OUTPUT_PATH, JSON_OUTPUT_FILE)
    py_file_path = os.path.join(COMPANIES_OUTPUT_PATH, PY_OUTPUT_FILE)

    store_json_data(tase_dict, json_file_path)
    store_dict_data(tase_dict, py_file_path)

    print(f"Created files: '{json_file_path}', and '{py_file_path}'")


if __name__ == '__main__':
    tase_api = TASE()
    tase_companies_dict = tase_api.companies_list()
    save_to_file(tase_companies_dict)
