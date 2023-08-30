user_name = input("What is your name? ")
date = str(input("Please enter your date of birth (Day/Month/Year): "))

foo = date.split("/")  # I wanted a more elegant way to get the year separate from the user inputted string. Split turns the string into a list of day, month, and year.  

age = 2023 - int(foo[2])
print(f"Hello {user_name}. According to your birthday, you are {age} years old.")