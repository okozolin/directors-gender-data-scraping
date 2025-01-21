__author__ = 'Orit Kozolin'

import requests
from config import TASE_API_KEY
from public_companies.api.config_api import TASE_COMPANIES_URL, TASE_DIRECTORS_URL
from public_companies.data.companies_api_output.api_output import companies_dict


class TASE(object):
    """Tel-Aviv Stock Exchange API requests"""

    def __init__(self):
        self.headers = {
            'accept': "application/json",
            'accept-language': "he-IL",
            'apikey': TASE_API_KEY
        }

    def companies_list(self):
        """
        List of TASE companies.
        API returns:
            companyName
            taseSector
            companyFullName
            issuerId
            corporateId
            isDual

        method returns a dictionary
        """

        response = requests.get(TASE_COMPANIES_URL, headers=self.headers)
        output = response.json()
        tase_companies_dict = {"taseCompanies": []}

        for company in output['companiesList']['result']:
            company_info = {'companyName': company['companyName'],
                            'companyFullName': company['companyFullName'],
                            'companyID': company['issuerId'],
                            'taseSector': company['taseSector'],
                            'corporateId': company['corporateId'],
                            'isDual': company['isDual'],
                            }
            tase_companies_dict['taseCompanies'].append(company_info)
        # print(tase_companies_dict)
        return tase_companies_dict

    def directors_list(self):
        """
        List of TASE directors.
        API returns:
            issuerId,
            issuerName,
            name,
            id
            position
            auditCommittee
            financialExpert
        method returns a dictionary {[companyName]:[ID]}
        """

        tase_directors_dict = {"taseDirectors": []}
        companies = companies_dict['taseCompanies']
        for company in companies:
            url = TASE_DIRECTORS_URL + str(company['companyID'])
            response = requests.get(url, headers=self.headers)
            output = response.json()
            director = output['getBoardAndManagementPositions']['result']
            keys = ['issuerId', 'issuerName', 'name', 'id','position', 'auditCommittee', 'financialExpert']
            director_info = {key: director[key] for key in keys}
            tase_directors_dict['taseDirectors'].append(director_info)

