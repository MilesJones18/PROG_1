import re



pattern = r"^([A-Z]{1,})[A-z0-9]{8,}$"

print("Please enter a password\nMust include:\n* 8-21 characters\n* Letters & numbers\n* Upper & lowercase\n* Special characters (@#$%*!)")
while True:
    usr_inpt = input("$ ")

    if re.search(pattern, usr_inpt):
        print("That is a valid password.")
        break

    else:
        print("That is not a valid password, please try again.")