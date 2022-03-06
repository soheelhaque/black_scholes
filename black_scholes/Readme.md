# Prerequisites
* Python 3.8.6 is installed
* pip is installed
* venv is installed
* VS Code is installed
* python is on your path (or you can open a shell where python is on the path)

# Installation
* Download the code from github at https://github.com/soheelhaque/black_scholes.git
* Create a virtual environment

    `python -m venv path/to/virtual/environment`
* Start up VS Code
* Point VS Code to your venv directory (optional)
  * Click on settings
  * Search for "venv"
  * Add the directory that contains your virtual environments
* Click on the View > Command Palette
* Type in "Python: Select Interpreter" and select or enter the path to the interpreter in the virtual environment you created
* In the terminal window, install requirements by typing in

    `pip install -r requirements.txt`

# Testing the Installation
* Click on the Testing icon in the left hand side. It looks like a conical flask
* Run all tests by clickin on the green triangle next to "tests"
* If you can't see any tests, click on the Explorer icon and open tests/test_calculator.py. 
* Right click and select "Run Current Test File", and switch to the output tab to see if there were any problems

# Running Black-Scholes
* Open app.py
* Click on Run > Run Without Debugging
* Open a browser and navigate to http://localhost:5000
* To test the REST API directly, navigate to http://localhost:5000/api/ui

Soheel Haque-Everding 2022