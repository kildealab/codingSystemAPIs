from Authentication import *
from config import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# NOTE: for production, you should probably not disable these warnings

# Global variables to store authentication tokens and headers for API requests 
# This is done so that they aren't authenticated on import for the cases in which someone only wants to use one of them
# ICD
icd_token = None 
icd_headers = None 

# UMLS
umls_auth_client = None 
umls_tgt = None


# ICD Authentication
def authenticate_icd():
    global icd_token, icd_headers
    if icd_token == None:
        # Token
        r = requests.post(token_endpoint, data=payload, verify=False).json()
        icd_token = r['access_token']

        # Headers for API requests
        icd_headers = {
            'Authorization': 'Bearer ' + icd_token,
            'Accept': 'application/json',
            'Accept-Language': 'en',
            'API-Version': 'v2'
        }

# UMLS Authentication
def authenticate_umls():
    global umls_auth_client, umls_tgt
    if umls_auth_client == None:
        AuthClient = Authentication(umls_api_key) 
        tgt = AuthClient.gettgt()




sct_headers = {'Authorization':  'Basic', 
           'Accept': 'application/json', 
           'Accept-Language': 'en',
        'API-Version': 'v2',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.62'}


def get_icd_display(code, lang):
    # Note: for ICD language codes supported: https://icd.who.int/icdapi/docs2/SupportedClassifications/
    authenticate_icd()
    uri = 'https://id.who.int/icd/'+icd_version+'/' + code  # access ICD API --> can update version here
    icd_headers['Accept-Language'] = lang # Set header field to desired language  
    r = requests.get(uri, headers=icd_headers, verify=False) # make request 

    if 'Requested resource could not be found' in r.text:
        print("WARNING: No response received for code",code,"in",lang)
        return '' # Return empty string if no reponse received found

    response = r.json()
    return response['title']['@value']

def get_snomed_display(code, lang):
    uri = 'https://browser.ihtsdotools.org/snowstorm/snomed-ct/browser/'+snomed_edition+'/'+snomed_version+'/concepts/' + code # access snomed API
    sct_headers['Accept-Language'] = lang # Set header field to desired language
    r = requests.get(uri, headers=sct_headers, verify=False) # make request
    print(r.text)
    if 'Concept not found' in r.text:
        print("WARNING: No response received for code",code,"in",lang)
        return '' # Return empty string if no reponse received found       
    
    response = r.json()
    return response['pt']['term'].replace("'","''") if lang in response['pt']['lang'] else ''

def get_umls_display(code, lang):
    authenticate_umls()
    base_uri = "https://uts-ws.nlm.nih.gov/rest"
    endpoint = "/content/" + umls_version + "/CUI/" + code + "/atoms"
    # query = {'ticket':AuthClient.getst(tgt)}
    query = {'apiKey':umls_api_key}
    # If not english, must search for the code's atoms that have the given language
    # Can add more statements if other languages included
    if "fr" in lang.lower():
        endpoint = endpoint + "?language=FRE"
    elif "en" in lang.lower():
        endpoint = endpoint+"?language=ENG"
    else:
        endpoint = endpoint+"?language="+lang

    r = requests.get(base_uri+endpoint, params=query,verify=False)
    
    if ('No results' in r.text):
        print("WARNING: No response received for code",code,"in",lang)
        return '' # Return empty string if no reponse received found   

    response = r.json()
    return response['result'][0]['name']   

