# codingSystemAPIs
This repository contains Python code that allows you to retrieve and display the medical code names for ICD-10, SNOMED CT, and UMLS coding systems in various languages. 
This code can be used as an example for how to use the ICD, SNOMED and UMLS APIs in Python. 

## Table of Contents
- [Motivation](#Motivation)
- [Files](#Files)
- [Prerequesites](#Prerequesites)
- [Installation](#Installation)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [Contact](#Contact)
- [Disclaimer](#Disclaimer)
  
## Motivation
Coding systems like ICD, SNOMED, and UMLS are excellent tools for standardizing medical nomenclature and ensuring consistency in medical documentation across various languages.
However, medical records typically only store code display names in a single language, and, given that we are a centre located in Québec, Canada, display names often need to be translated between and displayed in both French and English. 
Therefore, this tool was created to facilitate the retrieval of medical code display names in any language using the coding systems' APIs. 

## Files
* `get_display_name.py`: Contains functions to retrieve display names for medical codes from ICD-10, SNOMED CT, and UMLS APIs.
* `Authentication.py`: Handles UMLS API authentication using an API key.
* `config.py`: Contains configuration variables for accessing the ICD-10 and UMLS APIs.
* `requirements.txt`: The required python packages.
* `Example.py`: Demonstrates how to use the functions in `get_display_name.py`.

## Prerequesites
### Dependencies
* Python >= 3.8
* lxml >= 5.3.0
* 
### API Access Credentials
* **ICD-10**: Register at https://icd.who.int/icdapi (see "API ACCESS") to get an access token.
* **UMLS**: Register at https://documentation.uts.nlm.nih.gov/rest/home.html (click "Get Your API Key") to get an API key.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/kildealab/codingSystemAPIs.git
   ```
2. Install dependenices:
   ```
   cd codingSystemAPIs
   pip install -r requirements.txt
   ```
## Usage
1. **Set up configuration**: Update the `config.py` file with your API credentials. Specifically, you will need to change:
    * For ICD: `client_id` and `client_secret`
    * For UMLS: `umls_api_key`
2. **Retrive coding names**: Import `get_display_name` and use the following function calls in your code to retrieve the display name in any language from the code. An example usage is shown in `Example.py`.
    ```
    from get_display_name import get_icd10_display, get_snomed_display, get_umls_display

    get_icd10_display(code="C77.0", lang='fr')) # ICD-10 Example
    get_snomed_display(code="774007", lang='fr')) # SNOMED-CT Example
    get_umls_display(code="C0155502", lang='FRE')) # UMLS Example
    ```

## Contributing
We welcome contributions! If you are interested in contributing, please fork the repository and create a pull request with your changes.
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them.
4. Push your branch: `git push origin feature-name`
5. Create a pull request.

## Lincense

## Contact
For support or questions, please email Kayla O'Sullivan-Steben at kayla.osullivan-steben@mail.mcgill.ca.
