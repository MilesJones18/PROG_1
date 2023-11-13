import re


pattern = r"^([0-9]{3}+-)([0-9]{3}+-)([0-9]{4})$"

phone_number = input("Please enter your phone number (xxx-xxx-xxxx): ")


if re.match(pattern, phone_number):
    print("That number is valid.")

else:
    print("That number is not valid.")