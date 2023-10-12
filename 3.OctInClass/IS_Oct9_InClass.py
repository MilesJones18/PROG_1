'''
String manipulation

'''

# letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# letters2 = 'abcdefghijklmnopqrstuvwxyz'

# char = input('What letter would you like to look for? ')

# if char in letters2:
#     print("That letter is in the string.")

# else:
#     print("That letter is not in the string.")



# phrase = '99 Red Balloons'
# position = phrase.find("Red")

# if position != -1:
#     print(f"The word was contained at position {position}")



# filename = input("")

# # loop through all files in a directory
# if filename.endswith('.txt'):
#     print("The file you are looking for is a text file.")

# else:
#     print("That is not a text file.")


# # replacing values
# newPhrase = phrase.replace("Balloons", "apples")
# print(newPhrase)


# result = letters.lower()
# print(result)

# result2 = letters2.upper()
# print(result2)


# string testing methods

def is_special(word):
    specialChar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '~']

    for char in word:
        if char in specialChar:
            return True
        else:
            continue

def menu():
    user_choice = input("Please enter a passphrase: ")

    if user_choice.isalnum():
        print("The string is alphanumeric")

    if user_choice.isdigit():
        print("The string contains only numbers")

    if user_choice.isalpha():
        print("The string contains only letters")

    if user_choice.islower():
        print("The string is lowercase")

    if user_choice.isupper():
        print("The string is uppercase")

    if is_special(user_choice) == True:
        print("The string contains special characters")


if __name__ == "__main__":
    menu()