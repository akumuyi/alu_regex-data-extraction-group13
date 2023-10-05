# Regex Data Extraction Hackathon

Welcome to the Regex Data Extraction Hackathon! This project involves extracting specific data types from raw API responses using regular expressions. The goal is to efficiently extract various data types, such as restaurant names, ingredient lists, RGB color values, social media usernames, product codes, news headlines, event dates and times, and email addresses, from unstructured text data.

## Team Information

- **Team Name:** Group 13
  
- **Team Members:**
  - Abiodun Kumuyi (GitHub Username: akumuyi)
  - Divine Ishimwe (GitHub Username: IBIRASA)
  - Albertine Ingabire (Github Username: Ialbertine)
  - Josephine Mutesi (GitHub Username: josephine324)
  - Michael George (GitHub Username: MLEGION)

## Project Structure

The project repository is organized as follows:

- `py_modules/`: This directory contains the python packages for data extraction tasks.
    - 'Product-codes.py': Extracts product codes from raw/unstructured data.
    - 'email-address.py': Extracts valid email addresses from raw/unstructured data.
    - 'event-date-time.py': Extracts even, date, and time items from raw/unstructured data that meets the pattern requirements "MMM DD, YYYY - hh:mm AM/PM".
    - 'name-cuisines.py': Extracts restuarant names and the available cuisines from raw/unstructured data.
    - 'username.py': Extracts usernames/monikers starting with '@' from raw/unstructured data.
      
- `txt_vault/`: This directory contains the text data files used in testin the scripts.
    - 'Email-Address.txt': Contains thousands of valid and invalid email address.
    - 'Event-Date-Time.txt': Contains a body of text about different events detailing their times and dates of occurence.
    - 'Name-Cuisine.txt': Contains details of multiple restaurant and the meals they serve.
    - 'Product-Codes.txt': Contains product reviews of many different products.
    - 'Username.txt': Contains reviews about multiple social media users.
    - 'email-gen.py': Contains the python script to randomly generate over a thousand email addresses, mixing the list up with valid and invalid emails.

- `README.md`: This README file provides an overview of the project and instructions.

  
## Challenges

For this hackathon, we have chosen to work on the following challenges:

1. **Restaurant Names and Cuisine Types**
   - Description: Extract restaurant names and cuisine types from raw text.
   - Implementation: Python
   - Regex Pattern: re.compile(r"(?P<name>\w+(?:\s+\w+)*)\s+-\s+(?P<cuisine>\w+)")

2. **Social Media Usernames**
   - Description: Extract social media usernames from raw text.
   - Implementation: Python
   - Regex Pattern: re.compile(r"@[^\s]+")

3. **Product Codes**
   - Description: Extract product codes from raw text.
   - Implementation: Python
   - Regex Pattern: r'\b[A-Z]{3}\d{3}\b'

4. **Event Dates and Times**
   - Description: Extract event dates and times from raw text.
   - Implementation: Python
   - Regex Pattern: re.compile(r"(?P<month>\w{3}) (?P<day>\d{2}), (?P<year>\d{4}) - (?P<hour>\d{2}):(?P<minute>\d{2}) (?P<am_pm>\w{2})")
     
5. **Email Addresses**
   - Description: Extract email addresses from raw text.
   - Implementation: Python
   - Regex Pattern: re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")

## Usage

You can use the provided regex patterns and code snippets to extract data types from your API responses or text data. Each challenge corresponds to a specific data type, and the regex patterns are designed to match common patterns for that data type.

To get started with a specific challenge, navigate to the root folder on your terminal and enter the prompt "python3 py_modules/'desired_python_package'" (depending on the data type you are trying to extract for your use case.


