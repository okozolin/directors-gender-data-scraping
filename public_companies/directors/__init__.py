from config import DIRECTORS_OUTPUT_PATH
from public_companies.api.tase_api import TASE
from public_companies.companies import save_to_file

if __name__ == '__main__':
    tase_api = TASE()
    tase_directors_dict = tase_api.directors_list()
    save_to_file(tase_directors_dict, DIRECTORS_OUTPUT_PATH)
