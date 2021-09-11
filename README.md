# CompleteFramework

To create virtual environment called "venv":

virtualenv env

===============================================================

To enter virtual environment called "venv":

source venv/Scripts/activate

===============================================================

To quit virtual environment (first we have to be on the virtual environment):

deactivate

===============================================================

To delete virtual environment called "venv":

rm -r venv/

===============================================================

To install requirements in the virtual env:

source venv/Scripts/activate

pip install -r requirements.txt

===============================================================

rm -r ./resources/reports/

pytest -m ${tag_name} -v -s --browser=${browser} --alluredir= ${allure_report_path}

pytest -m regression -v -s --browser=edge --alluredir=./resources/reports/my-allure-results

===============================================================

To see allure results:

allure serve ./tests/resources/reports/
