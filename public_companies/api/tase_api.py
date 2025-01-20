__author__ = 'Orit Kozolin'

import requests
from config import TASE_API_KEY
from public_companies.api.config_api import TASE_COMPANIES_URL


class TASE(object):
    """Tel-Aviv Stock Exchange API requests"""

    def companies_list(self):
        """
        List of TASE companies.
        API returns: company Name, Sector, issuerID, corporateID
        method returns a dictionary {[companyName]:[ID]}
        """

        headers = {
            'accept': "application/json",
            'accept-language': "he-IL",
            'apikey': TASE_API_KEY
        }
        response = requests.get(TASE_COMPANIES_URL, headers=headers)
        output = response.json()
        tase_companies_dict = {"taseCompanies": []}

        for company in output['companiesList']['result']:
            company_info = {'companyName': company['companyName'],
                            'companyID': company['issuerId'],
                            'taseSector': company['taseSector']}
            tase_companies_dict['taseCompanies'].append(company_info)
        # print(tase_companies_dict)
        return tase_companies_dict
