import random
import string

# Function to generate a random valid email address
def generate_valid_email():
    domains = ["com", "net", "org", "gov", "edu"]
    domain = random.choice(domains)
    username_length = random.randint(5, 10)
    username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(username_length))
    return f"{username}@example.{domain}"

# Function to generate a random invalid email address
def generate_invalid_email():
    email_length = random.randint(5, 20)
    email = ''.join(random.choice(string.ascii_lowercase + string.digits + "!@#$%^&*()") for _ in range(email_length))
    return email

# Generate 60% valid and 40% invalid email addresses
num_valid_emails = 120
num_invalid_emails = 80

valid_emails = [generate_valid_email() for _ in range(num_valid_emails)]
invalid_emails = [generate_invalid_email() for _ in range(num_invalid_emails)]

# Combine valid and invalid emails
all_emails = valid_emails + invalid_emails

# Shuffle the list of emails
random.shuffle(all_emails)

# Write the emails to a text file
with open("Email-Address.txt", "w") as file:
    file.write("\n".join(all_emails))

print("Emails generated and saved to 'Email-Address.txt'.")
