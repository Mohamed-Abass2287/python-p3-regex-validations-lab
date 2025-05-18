import re

# Regular expression for names: Allows letters, spaces, hyphens, apostrophes, and ensures proper capitalization
name = r"^[A-Z][a-zA-Z\s'-]{1,49}$"
name_regex = re.compile(name)

# Regular expression for phone numbers: Supports various formats including international numbers with parentheses
phone_number = r"^\+?\d{1,4}?[\s.-]?\(?\d{2,4}\)?[\s.-]?\d{3,4}[\s.-]?\d{4}$"
phone_regex = re.compile(phone_number)

# Regular expression for email addresses: Ensures that an email starts with an alphabet character
email_address = r"^[a-zA-Z][a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)

# Updated test cases
test_names = ["John Doe", "Anne-Marie", "O'Connor", "john cena", "D'Angelo", "John   Cena"]
test_phones = ["+1234567890", "(555) 555-5555", "555-555-5555", "555555555", "aaaaaaaaaa"]
test_emails = ["test@example.com", "user.name+tag@domain.co.uk", "123john.cena@wwe.com", "invalid-email@", "name@domain"]

# Validate test cases
for name in test_names:
    print(f"Name '{name}' valid? {bool(name_regex.match(name))}")

for phone in test_phones:
    print(f"Phone '{phone}' valid? {bool(phone_regex.match(phone))}")

for email in test_emails:
    print(f"Email '{email}' valid? {bool(email_regex.match(email))}")
