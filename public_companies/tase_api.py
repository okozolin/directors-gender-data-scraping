__author__ = 'Orit Kozolin'

import requests
from config import TASE_API_KEY
from public_companies.helpers.file_handler import store_json_data, dict_to_file


class TASE(object):
    """Tel-Aviv Stock Exchange API requests"""

    base_url = 'https://datawise.tase.co.il'

    def companies_list(self):
        """
        List of TASE companies.
        API returns: company Name, Sector, issuerID, corporateID
        method returns a dictionary {[companyName]:[ID]}
        """
        url = self.base_url + "/v1/basic-securities/companies-list"
        headers = {
            'accept': "application/json",
            'accept-language': "he-IL",
            'apikey': TASE_API_KEY
        }
        response = requests.get(url, headers=headers)
        output = response.json()
        tase_companies_dict = {"taseCompanies": []}

        for company in output['companiesList']['result']:
            company_info = {'companyName': company['companyName'],
                            'companyID': company['issuerId'],
                            'taseSector': company['taseSector']}
            tase_companies_dict['taseCompanies'].append(company_info)
        # print(tase_companies_dict)
        return tase_companies_dict

if __name__ == '__main__':
    tase_api = TASE()
    tase_companies_dict = tase_api.companies_list()
    output_path = "data/companies_api_output"

    store_json_data(tase_companies_dict,f"{output_path}/api_output.json")
    dict_to_file(tase_companies_dict, f"{output_path}/api_output.py")