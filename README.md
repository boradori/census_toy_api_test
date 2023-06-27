# Census Toy API Test

## Dependencies
```pytest, pytest-html, requests```

In order to run this test, you will need to install **Python** and **pip** first. **pip** is
a **Python package manager** that allows you to install and manage software packages written in **Python**.

If you install **Python**, **pip** will also be automatically installed.

Clone this repo and enter project directory!
```commandline
git clone https://github.com/boradori/census_toy_api_test.git
```

```commandline
cd census_toy_api_test
```

You should also use virtual environment for easier dependency management of your project. Please try to use the following command to create a virtual environment.
```commandline
python -m venv venv
or
python3 -m venv venv
```

Once you have created a virtual environment, you can activate it by using the following command.
```commandline
source venv/bin/activate
```

Then, you can use the following command to install dependencies.
```commandline
pip install -r requirements.txt
```

## Execution
There are multiple ways to execute the test for different purposes.

### Execute all test cases
```commandline
pytest
```

### Execute all test cases and generate a report
```commandline
pytest --html=reports.html
```

### Execute test_count_by_gender
```commandline
pytest -m count_by_gender
```
with 'top' value to limit the number of results
```commandline
pytest -m count_by_gender --top_gender=1
```

### Execute test_count_by_country
```commandline
pytest -m count_by_country
```
with 'top' value to limit the number of results
```commandline
pytest -m count_by_country --top_country=3
```

### Execute test_count_password_complexity
```commandline
pytest -m count_password_complexity
```
with 'top' value to limit the number of results
```commandline
pytest -m count_password_complexity --top_pw_complex=4
```

You can also apply 'top' values when running the entire test suite.
```commandline
pytest --top_gender=2 --top_country=4 --top_pw_complex=3 --html=reports.html
```

## What I tested and how
- I tested Census Toy API with **pytest** and **requests**.
- There are three ActionTypes, **CountByGender**, **CountByCountry**, and **CountPasswordComplexity**.
- **top** values can be added via CLI to limit the number of results; 'top' values are optional and default values are 5.
- I made combinations of **top** value and the number of users using CLI and **parametrize** decorator.
- I made a **test_utils.py** file to store common functions that are used in multiple test cases.
- I used pytest's **parametrize** decorator to run the same test with different parameters for positive and negative tests.
- Negative tests are **invalid users list**, **invalid action type**, and **no action type** for 400 status code.
- test cases also focus on positive and negative test cases. Please refer to test cases for more information.

## Test Cases
I made a separate document for test cases. Please refer to the following link.
https://docs.google.com/document/d/1ok_aSfwVwfojXwYywBlBxI2qiFJ3Q_bbQ0YWnfl9gCQ/edit?usp=sharing

## Bug Report
I made a separate document for bug report. Please refer to the following link.
https://docs.google.com/document/d/1T1ozqChipvaxPZd3_AXj68jbJ8MQE2pYs5ZerLlf3dY/edit?usp=sharing