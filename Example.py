# Filename: Example.py
# Author: Kayla O'Sullivan-Steben
# Date Created: January 21, 2025
# Description: Provides examples using the code in code_api_requests. 

from code_api_requests import get_icd_display, get_snomed_display, get_umls_display
    
# Example ICD 10
 
try:
	code = "C77.0"
	language = 'fr'
	print("ICD -",code,"=",get_icd_display(code, language))
	
except Exception as e:
	print("Error with ICD-10",e)


# Example SNOMED
try:
	code = "774007"
	language = 'fr' # For Canadian SNOMED, languages are 'fr' and 'en'
	print("SNOMED-CT -",code,"=",get_snomed_display(code, language))
except Exception as e:
	print("Error with SNOMED-CT",e)

# Example UMLS
try:
	code = "C0155502"
	language = 'FRE'# Languages allowed for UMLS:“ENG”,“FRE”,“SPA”,“GER”,“DUT”,“JPN”, etc
	print("UMLS - ",code,"=",get_umls_display(code, language)) 
except Exception as e:
	print("Error with UMLS:", e)


# Example ICD-11
# NOTE: must set icd_version = 'entity' in config.py, then uncomment below 
 
# try:
# 	code = "257068234"#"C77.0"
# 	language = 'es' # Current languages allowed in latest version 2024-01: ar, cs, en, es, fr, pt, ru, tr, uz, zh
# 	print("ICD:",get_icd10_display(code, language))
# except Exception as e:
# 	print("Error with ICD-11",e)
