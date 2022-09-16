import requests
from requests.structures import CaseInsensitiveDict

import sys
try:
    sys.path.insert(1, 'F:\Python\__My Python Programs\CSV Converter')
    from CSVConverter import CSVConverter
except:
    sys.path.insert(1, 'C:/Users/magnu/s/Python310/My Python3_10 Programs/CSV Converter')
    from CSVConverter import CSVConverter

class APItools:
    def __init__(self):
        self.CC = CSVConverter()
        self.headers_dict = {'Solscan': {'User-Agent': 'My User Agent 1.0', \
                                         'From': 'youremail@domain.example'}}
        self.URL_dict = {'Solscan': {'token': {'meta': 'https://public-api.solscan.io/token/meta?tokenAddress='}, \
                                     'market': {'token': 'https://public-api-test.solscan.io/market/token/'}, \
                                     'account': {'transactions': 'https://public-api.solscan.io/account/transactions?account=', \
                                                 'exportTransactions': 'https://public-api.solscan.io/account/exportTransactions?account=<ADDRESS>&type=all&fromTime=0&toTime=10000000000000000000'}}}

    def request(self, URL, headers, output_type='json', file_name='API_response'):
        response = requests.get(URL, headers=headers)
        try:
            response = response.json()
            json_file = True
        except:
            json_file = False
        if output_type == 'csv':
            if json_file:
                response = self.CC.convertJSONtoCSV(response)
            else:
                response = self.CC.convertBytesToCSV(response, file_name=file_name)
        return(response)

    

shit = 'balls'



