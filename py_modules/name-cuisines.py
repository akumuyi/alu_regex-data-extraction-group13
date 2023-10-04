import re

# Open the Name-Cuisine.txt file for reading
with open("/alu_regex-data-extraction-group13/txt_vault/name-Cuisine.txt", "r") as f:
    # Read the entire file contents into a string
    text = f.read()

# Compile the regular expression for extracting restaurant Names and Cuisines
name_cuisine_regex = re.compile(r"(?P<name>\w+(?:\s+\w+)*)\s+-\s+(?P<cuisine>\w+)")

# Extract all of the restaurant names and cuisines from the text
name_cuisine_lists = name_cuisine_regex.findall(text)

# Print the extracted restaurant names and cuisines
for name_cuisine_list in name_cuisine_lists:
    print(f"{name_cuisine_list[0]}: {name_cuisine_list[1]}")
