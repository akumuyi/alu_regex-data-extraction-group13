import re

# Open the Email-Address.txt file for reading
with open("/alu_regex-data-extraction-group13/txt_vault/Email-Address.txt", "r") as f:
    # Read the entire file contents into a string
    text = f.read()

# Compile the regular expression for extracting email addresses
email_regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")

# Extract all of the email addresses from the text
email_addresses = email_regex.findall(text)

# Print the extracted email addresses
for email_address in email_addresses:
    print(email_address)

