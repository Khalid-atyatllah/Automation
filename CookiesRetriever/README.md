# CookiesRetriever

## Overview
CookiesRetriever is a Selenium automation project designed to automate the login process and retrieve cookies from websites. It saves time by avoiding the need to manually log in every time you test automated processes.

## Project Structure
The project consists of modularized components:

- **chrome_options.py**: Defines Chrome options for WebDriver setup.
- **webdriver_setup.py**: Initializes the Chrome WebDriver.
- **login_process.py**: Contains the logic for manual login and cookie retrieval.
- **cleanup.py**: Handles cleanup operations for the WebDriver.

## Usage
1. Ensure Python 3.x is installed.
2. Install necessary libraries:
   ```bash
   pip install selenium pandas
