"""1) Explore more regex patterns Eg. The regex pattern used to validate email addresses, mobile no, string, and more"""
# include <iostream>
# include <regex>
import re

email = "abc@gmail.com"
mobile = "9876543210"
password = "Anmol@123"

email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
mobile_pattern = r'^[6-9]\d{9}$'
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

print("Email:", bool(re.match(email_pattern, email)))
print("Mobile:", bool(re.match(mobile_pattern, mobile)))
print("Password:", bool(re.match(password_pattern, password)))
