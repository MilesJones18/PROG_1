user_name = input("What is your name? ")  # Stores the users input into the user_name variable.
date = str(input("Please enter your date of birth (Day/Month/Year): "))  # Stores the users input as a str in the date variable.


foo = date.split("/")  # I wanted a more elegant way to get the year separate from the user inputted string. Split turns the string into a list of day, month, and year.  


age = 2023 - int(foo[2])  # Subtracts the year that the user inputs from the current year, since the year is originally a string, it is converted into an integer.
print(f"Hello {user_name}. According to your birthday, you are {age} years old.")  # Prints the user_name variable as well as the new age variable.