'''User types 1 or 2, if 1, execute while loop that continues until 100, if 2, Shoot 100 baskets.'''
import random


user_choice = input("Please enter a 1 or 2: ")


if user_choice == "1":
    num_made = 0
    trys = 0
    while(num_made != 101):
        num_made = random.randint(0, 101)
        trys += 1

    print(f"Trys: {trys}")



if user_choice == "2":
    trys = 0
    for i in range(0, 101):
        num_made = random.randint(0, 2)
        if (num_made == 0):
            continue
        else:
            trys += 1
    print(f"Trys: {trys}")