user_input = int(input("What is your current age?: "))

if user_input >= 18:
    print("Senior")

elif user_input >= 16:
    print("Normal")

elif user_input >= 12:
    print("Junior")

else:
    print("You're too young")