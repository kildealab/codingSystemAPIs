##########################################################
# ICD API access variables
# To get an access token, you must register at: https://icd.who.int/icdapi (see "API ACCESS")
token_endpoint = 'https://icdaccessmanagement.who.int/connect/token'
client_id = 'client id here'
client_secret = 'client secret here'
scope = 'icdapi_access'
grant_type = 'client_credentials'

payload = {'client_id': client_id, 
        'client_secret': client_secret, 
        'scope': scope, 
        'grant_type': grant_type}

##########################################################
# UMLS API access variables
# To get an API key, you will need to register at: https://documentation.uts.nlm.nih.gov/rest/home.html (click "Get Your API Key")
umls_api_key =  'api key here'

##########################################################
# SNOMED access variables 
# N/A