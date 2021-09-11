# SeleniumPythonEx1
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

To install requeriments in the virtual env:

source venv/Scripts/activate

pip install -r requirements.txt

===============================================================

We can specify the browser by adding --browser "browser_name"

browser names available: "chrome", "firefox", "edge"

Example: pytest -v -s --browser chrome

===============================================================

Command to run php travels test only (group):

pytest -m php_travels -v -s

===============================================================

Command to run heroku app test only (group):

$ pytest -m heroku_app -v -s

===============================================================

Command to see allure report:

pytest --alluredir=./my_allure_results

===============================================================

To see allure results:

allure serve ./my_allure_results
