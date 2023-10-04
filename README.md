# Regex Data Extraction Hackathon

Welcome to the Regex Data Extraction Hackathon! This project involves extracting specific data types from raw API responses using regular expressions. The goal is to efficiently extract various data types, such as restaurant names, ingredient lists, RGB color values, social media usernames, product codes, news headlines, event dates and times, and email addresses, from unstructured text data.

## Team Information

- **Team Name:** Group 13
- **Team Members:**
  - Abiodun Kumuyi (GitHub Username: akumuyi)
  - Member 2 (GitHub Username)

## Project Structure

The project repository is organized as follows:

- `py_modules/`: This directory contains the python packages for data extraction tasks.
- `txt_vault/`: This directory contains the text data files used in testin the scripts.
- `README.md`: This README file provides an overview of the project and instructions.
## Challenges

For this hackathon, we have chosen to work on the following challenges:

1. **Restaurant Names and Cuisine Types**
   - Description: Extract restaurant names and cuisine types from raw text.
   - Implementation: Python/JavaScript
   - Regex Pattern: `r"(.+) - (.+)"`

2. **Ingredient Lists**
   - Description: Extract ingredient lists from raw text.
   - Implementation: Python/JavaScript
   - Regex Pattern: `r"([^,]+)(?:,|$)"`

3. **RGB Color Values**
   - Description: Extract RGB color values from raw text.
   - Implementation: Python/JavaScript
   - Regex Pattern: `r"rgb\((\d+), (\d+), (\d+)\)"`

4. **Social Media Usernames**
   - Description: Extract social media usernames from raw text.
   - Implementation: Python/JavaScript
   - Regex Pattern: `r"@(\w+)"`

5. **Product Codes**
   - Description: Extract product codes from raw text.
   - Implementation: Python/JavaScript
   - Regex Pattern: `r"([A-Z]{3}\d{3})"`

6. **News Headlines**
   - Description: Extract news headlines and subheaders from raw text.
   - Implementation: Python/JavaScript
   - Regex Pattern: `r"(.+): (.+)"`

7. **Event Dates and Times**
   - Description: Extract event dates and times from raw text.
   - Implementation: Python/JavaScript
   - Regex Pattern: `r"(\w{3} \d{2}, \d{4} - \d{2}:\d{2} [APap][Mm])"`

8. **Email Addresses**
   - Description: Extract email addresses from raw text.
   - Implementation: Python/JavaScript
   - Regex Pattern: `r"([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})"`

## Usage

You can use the provided regex patterns and code snippets to extract data types from your API responses or text data. Each challenge corresponds to a specific data type, and the regex patterns are designed to match common patterns for that data type.

To get started with a specific challenge, navigate to the root folder on your terminal and enter the prompt "python3 py_modules/'desired_python_package'" (depending on the data type you are trying to extract for your use case.

## Contributions

- Each team member is encouraged to contribute to the project by implementing and testing one or more of the data extraction challenges.
- Commit your code to this GitHub repository using your ALU email address.
- Ensure that every team member commits code at least once to track individual contributions.

