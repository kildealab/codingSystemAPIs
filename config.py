##########################################################
# ICD API access variables
token_endpoint = 'https://icdaccessmanagement.who.int/connect/token'
client_id = #'client id here'
client_secret = #'client secret here'
scope = 'icdapi_access'
grant_type = 'client_credentials'

payload = {'client_id': client_id, 
        'client_secret': client_secret, 
        'scope': scope, 
        'grant_type': grant_type}

##########################################################
# UMLS API access variables
umls_api_key =  'api key here'

##########################################################
# SNOMED access variables 
# N/A
   