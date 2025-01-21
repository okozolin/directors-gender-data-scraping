from config import COMPANIES_OUTPUT_PATH
from public_companies.helpers.file_handler import save_to_file
from public_companies.api.tase_api import TASE


if __name__ == '__main__':
    tase_api = TASE()
    tase_companies_dict = tase_api.companies_list()
    save_to_file(tase_companies_dict, COMPANIES_OUTPUT_PATH)
    # compare_companies_data(tase_companies_dict, excel_companies_list)
