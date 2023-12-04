'''
Regular Expressions


regex are used to typically match patterns. You have used them before if you search a PDF,
webpage, or Word Document for matching text.


A regular expression (regex) is a description for a pattern of text.
'''


import re


pattern = r"^[a-z]{1}:[a-z]{1}:[a-z]{1}$"  # creating a regex object using the raw string.

file_path = input("Enter the file path to test if it is valid: ")


if re.match(pattern, file_path):

    print("That is a valid filepath.")

else:
    print("That is not a valid filepath.")


pattern = r"^([A-z0-9]+:+\\)([A-z0-9]+\\)*([A-z0-9]+.txt|.zip)$"

file_path2 = input("Enter the file path to test if it is valid: ")


if re.match(pattern, file_path2):
    
    print("That is a valid filepath.")

else:
    print("That is not a valid filepath.")



