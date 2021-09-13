# CompleteFramework

* Url tested: 

        https://www.saucedemo.com/

* To create virtual environment called "venv":

        virtualenv env

* To enter virtual environment called "venv":

        source venv/Scripts/activate

* To quit virtual environment (first we have to be on the virtual environment):

        deactivate

* To delete virtual environment called "venv":

        rm -r venv/

* To install requirements in the virtual env:

        source venv/Scripts/activate
        pip install -r requirements.txt

* Run on commandline:

        pytest -m ${tag_name} --browser=${browser}

* Example:

        pytest -m regression --browser=edge

*if no browser then it will run chrome by default*

* To see allure results:

        allure serve resources/reports/my-allure-results/

* Jenkins shell script:

        virtualenv venv
        source venv/bin/activate
        pip install -r requirements.txt
        pytest -m ${group} --operative_system="${operative_system}" --os_version="${os_version}" --browser=${browser} --browser_version=${browser_version}
        deactivate
