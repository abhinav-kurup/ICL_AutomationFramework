ICL Automation Framework

Overview
This repository contains a robust automation framework built using Pytest for testing web applications, APIs, and database components. It follows best practices in test automation, ensuring maintainability, scalability, and reliability.


Features
- Pytest-based test execution
- Fixtures for reusable setup and teardown
- Parameterized tests for data-driven testing


Project Structure
ICL Automation/
|-- base/                               # base files
    |-- base_api.py
    |-- base_db.py
    |-- base_ui.py
|-- config                      # Configuration files
    |-- config.ini
|-- reusable_components         # reusable components to eb used across inetgrations
    |-- api
    |-- db
    |-- pages
|-- testdata                    # Test Data by applications
    |-- banner
    |-- kx
|-- tests                       # Test cases by integrations
    |-- azure
    |-- banner
    |-- banner_to_azure
    |-- conftest.py                 # Pytest configuration and fixtures
|-- utilities                           # Utility functions
    |-- config.utils.py
    |-- data_utils.py
    |-- logger_utils.py
    |-- project_utils.py
│-- requirements.txt                    # Project dependencies
│-- README.md                           # Project documentation


Naming Convention
To maintain consistency and readability across the framework, follow these naming conventions:
    - Directories: Use snake_case for directories (e.g., test_cases, page_objects).
    - Test Files: Must start with test_ and follow snake_case (e.g., test_login.py).
    - Test Functions: Must start with test_ and follow snake_case (e.g., test_valid_login).
    - Class Names: Use PascalCase (e.g., ConfigUtils, BannerloginPage).
    - Fixtures: Should be in snake_case (e.g., setup_browser).
    - Page Objects: py files to follow snake_case(e.g. student_creation.py) and class name to follow PascalCase (e.g., LoginPage).
    - Utility Functions: Use snake_case (e.g., config_utils).
    - Configuration Files: Use .ini, .env, or .json extensions where applicable.


Prerequisites
Ensure you have the following installed on your system:
    - Python 3.7+
    - pip (Python package installer)

Install dependencies:
    - pip install -r requirements.txt

Running Tests
    - pytest -s "path to the tests"