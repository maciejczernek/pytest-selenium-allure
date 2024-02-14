# Quick start 
1. Install the [Allure Report](https://allurereport.org/docs/gettingstarted-installation/)
1. Create a new virtual environment in the main folder
1. Activate the virtual environment
1. Install the required libraries from `\venv_requirements\requirements.txt`
1. Run tests from `\tests` folder

# Remarks
- Additional params:
   
  `--browser (default="ff", choices="chrome, ff")`
  
  `--headless (default="True")`
  
  `--resolution (default="1920,1080")`
  
- The report will be generated automatically in the `\test_results\allure-report`
- To open the report type (example from the main folder): `allure open .\test_results\allure-report`



