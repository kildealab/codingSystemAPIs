from get_display_name import get_icd10_display, get_snomed_display, get_umls_display
                
try:
	print("icd10:",get_icd10_display("C77.0",'fr'))
except Exception as e:
	print("Error with ICD-10",e)

# try:
# 	print("smoned:",get_snomed_display("774007",'fr'))
# except Exception as e:
# 	print("Error with SNOMED-CT",e)

try:
	print("umls:",get_umls_display("C0155502",'FRE')) # Languages allowed for UMLS:“ENG”,“FRE”,“SPA”,“GER”,“DUT”,“JPN”, etc
except Exception as e:
	print("Error with UMLS:", e)