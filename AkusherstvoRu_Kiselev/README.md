Introduction
------------

This repository contains  example of usage PageObject
pattern with Selenium and Python (PyTest + Selenium).

Files
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[pages/base.py](pages/base.py) contains PageObject pattern implementation for Python.

[pages/elements.py](pages/elements.py) contains helper class to define web elements on web pages.

[tests/test_akusherstvo_*.py](tests/test_akusherstvo_*.py) contains several smoke Web UI tests for Akusherstvo.ru (https://www.akusherstvo.ru/)
Exactly:
[tests/test_akusherstvo_cart.py](tests/test_akusherstvo_cart.py) contains several smoke Web UI tests for cart of Akusherstvo.ru
[tests/test_akusherstvo_search.py](tests/test_akusherstvo_search.py) contains several smoke Web UI tests related to the search string of Akusherstvo.ru
[tests/test_akusherstvo_submenu.py](tests/test_akusherstvo_submenu.py) contains several smoke Web UI tests on the submenu of the product catalog of Akusherstvo.ru

How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*.py
   
    ```

   ![alt text](example.png)


