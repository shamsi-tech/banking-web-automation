<<<<<<< HEAD
# ParaBank Automation Testing Project

## Project Overview

This project focuses on Manual Software Testing and Selenium Automation Testing of the ParaBank Banking Web Application.

The objective is to validate important banking functionalities, identify defects, execute test cases, and automate selected scenarios using Selenium WebDriver and Python.

## Application Under Test

- **Application:** ParaBank
- **Website:** https://parabank.parasoft.com/parabank/index.htm

## Tools & Technologies

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Visual Studio Code
- Microsoft Excel

## Manual Testing

Manual testing was performed on key banking functionalities.

Testing activities include:
- Test Case Design
- Test Execution
- Positive and Negative Testing
- Functional Testing
- Bug Reporting
- Expected vs Actual Result Verification

**Test Cases:** Available in the `Test-Cases` folder.

## Bug Reporting

Identified bugs were documented and reported using GitHub Issues.

## Automation Testing

Four test scenarios were automated using Selenium WebDriver and executed through Pytest.

| Test Scenario | Status |
|---|---|
| Login | Passed |
| Account Creation | Passed |
| Fund Transfer | Passed |
| Bill Payment | Passed |

## Test Execution

Install project dependencies:

```bash
python -m pip install -r requirements.txt
```

Run all automation tests:

```bash
python -m pytest -v
```

Generate HTML test report:

```bash
python -m pytest -v --html=Reports/report.html --self-contained-html
```

## Test Execution Results

Latest full-suite execution:

- Total Automated Tests: 4
- Passed: 4
- Failed: 0

## Project Structure

```text
ParaBank-Automation/
│
├── Automation/
│   ├── test_login.py
│   ├── test_account_creation.py
│   ├── test_transfer.py
│   └── test_bill_payment.py
│
├── Test-Cases/
│   └── ParaBank_Test_Cases.xlsx
│
├── Reports/
│   └── report.html
│
├── screenshots/
├── requirements.txt
├── .gitignore
└── README.md
```

## Disclaimer

This project was created for educational and portfolio purposes using the ParaBank demo application.