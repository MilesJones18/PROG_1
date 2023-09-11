"""
Repetition Structures

while/for loops

"""
# user controlled
choice = input("Do you want to play a game? ")  # Must establish a pre-condition.

while(choice.lower() == "yes" or choice.lower() == "y"):  # while loop (condition-controlled T/F)
    print("Welcome to my game.")
    choice = input("Do you want to play again?")

print("Goodbye")


# for-loop (count controlled)

# programmer controlled
for i in range(1, 11):  # Can declare variable in the loop.
    print(i)

print("\n-------------------------\n")

for num in [1, 2, 3, 4]:
    print(num)


# while true
while True:
    choice = input("Do you want to play a game again? ")
    if(choice.lower() == "no"):
        break
    else:
        continue