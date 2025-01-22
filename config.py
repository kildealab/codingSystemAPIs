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

#ICD version (for a list of supported versions: https://icd.who.int/docs/icd-api/SupportedClassifications/)
icd_version = 'release/10/2008' # set to 2008 release for fr/en. For current version of ICD 11, replace with: 'entity'

##########################################################
# UMLS API access variables
# To get an API key, you will need to register at: https://documentation.uts.nlm.nih.gov/rest/home.html (click "Get Your API Key")
umls_api_key =  'api key here'

#UMLS version
umls_version = 'current'

##########################################################
# SNOMED access variables
# N/A

#SNOMED version (for all version options: https://browser.ihtsdotools.org/?)
snomed_edition = 'MAIN'
snomed_version = 'SNOMEDCT-CA/2024-11-30' # Set to Canadian version

