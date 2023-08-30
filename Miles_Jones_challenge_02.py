user_name = input("What is your name? ")
date = str(input("Please enter your date of birth (Day/Month/Year): "))
   
user_year = int(date[6:10])  # Takes the date string that the user inputs slices the year out and turns it into an integer. 
age = 2023 - user_year


print(f"Hello {user_name}. According to your birthday, you are {age} years old.")