from Authentication import *
from config import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# ICD-10 Authentication
r = requests.post(token_endpoint, data=payload, verify=False).json()
icd_token = r['access_token']

# UMLS authentication
AuthClient = Authentication(umls_api_key) 
tgt = AuthClient.gettgt()

# Headers for API requests
icd_headers = {'Authorization':  'Bearer '+ icd_token, 
        'Accept': 'application/json', 
        'Accept-Language': 'en',
        'API-Version': 'v2'}

sct_headers = {'Authorization':  'Basic', 
           'Accept': 'application/json', 
           'Accept-Language': 'en',
        'API-Version': 'v2',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.62'}


def get_code_display(display, system, code, lang):
    # ICD-10
    # Note: for ICD language codes supported: https://icd.who.int/icdapi/docs2/SupportedClassifications/
    if ('icd-10' in system):
        uri = 'https://id.who.int/icd/release/10/2008/' + code  # access ICD API
        icd_headers['Accept-Language'] = lang # Set header field to desired language  
        r = requests.get(uri, headers=icd_headers, verify=False) # make request 
        
        if 'Requested resource could not be found' in r.text:
            return display if 'en' in lang else '' # Return the display coded in mCODE if lang set to english

        response = r.json()
        return response['title']['@value']


    elif ('snomed' in system):
        uri = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct/MAIN%2FSNOMEDCT-CA%2F2021-09-30/concepts/' + code # access snomed API
        sct_headers['Accept-Language'] = lang # Set header field to desired language
        r = requests.get(uri, headers=sct_headers, verify=False) # make request

        if 'Concept not found' in r.text:
            return display if 'en' in lang else '' # Return the display coded in mCODE if lang set to english          
        
        response = r.json()
        print(response)
        return response['pt']['term'].replace("'","''") if lang in response['pt']['lang'] else ''


    elif ('umls' in system):
        base_uri = "https://uts-ws.nlm.nih.gov/rest"
        endpoint = "/content/current/CUI/" + code
        query = {'ticket':AuthClient.getst(tgt)}

        # If not english, must search for the code's atoms that have the given language
        # Can add more statements if other languages included
        if "fr" in lang:
            endpoint = endpoint + "/atoms?language=FRE"

        r = requests.get(base_uri+endpoint, params=query)
        
        if ('No results' in r.text):
            return display if 'en' in lang else '' # Return the display coded in mCODE if lang set to english
        
        response = r.json()
        return response['result']['name'] if "en" in lang else response['result'][0]['name']           
                


get_code_display('test displace', 'snomed', '774007', 'FR')