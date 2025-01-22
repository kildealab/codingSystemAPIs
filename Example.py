from code_api_requests import get_icd_display, get_snomed_display, get_umls_display
    
# Example ICD 10
 
try:
	code = "C77.0"
	language = 'fr'
	print("ICD:",get_icd_display(code, language))
except Exception as e:
	print("Error with ICD-11",e)


# Example SNOMED
# try:
# 	code = "774007"
# 	language = 'fr'
# 	print("smoned:",get_snomed_display(code, language))
# except Exception as e:
# 	print("Error with SNOMED-CT",e)

# Example UMLS
try:
	code = "C0155502"
	language = 'FRE'# Languages allowed for UMLS:“ENG”,“FRE”,“SPA”,“GER”,“DUT”,“JPN”, etc
	print("UMLS:",get_umls_display(code, language)) 
except Exception as e:
	print("Error with UMLS:", e)


# Example ICD-11, must set icd_version = 'entity' in config.py, then uncomment     
# Current languages allowed in latest version 2024-01: ar, cs, en, es, fr, pt, ru, tr, uz, zh
 
# try:
# 	code = "257068234"#"C77.0"
# 	language = 'es'
# 	print("ICD:",get_icd10_display(code, language))
# except Exception as e:
# 	print("Error with ICD-11",e)
