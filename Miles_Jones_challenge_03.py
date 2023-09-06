correct = 0
incorrect = 0

print(f"      -------| Welcome to the Escape Room! |-------\nYou must get at least 3 correct in order to escape the room.\n")

rid1 =  input("What can you hold in your right hand, but never in your left hand? ")

if rid1.lower() == "your left hand":
    correct += 1
    print(f"Thats correct! ({correct}/5)\n")
else:
    incorrect += 1
    print(f"Sorry, thats incorrect. ({incorrect}/5)\n")


rid2 = input("What gets wet while drying? ")

if rid2.lower() == "a towel":
    correct += 1
    print(f"Thats correct ({correct}/5)\n")
else:
    incorrect += 1
    print(f"Sorry, thats incorrect ({incorrect}/5)\n")


rid3 = input("What kind of band never plays music? ")

if rid3.lower() == "a rubber band":
    correct += 1
    print(f"Thats correct! ({correct}/5)\n")
else:
    incorrect += 1
    print(f"Sorry, thats incorrect. ({incorrect}/5)\n")


rid4 = input("What is the end of everything? ")

if rid4.lower() == "g":
    correct += 1
    print(f"Thats correct! ({correct}/5)\n")
else:
    incorrect += 1
    print(f"Sorry, thats incorrect ({incorrect}/5)\n")


rid5 = input("When is a door no longer a door? ")

if rid5.lower() == "when it is ajar" or rid5.lower() == "when its ajar":
    correct += 1
    print(f"Thats correct! ({correct}/5)\n")
else:
    incorrect += 1
    print(f"Sorry, thats incorrect. ({incorrect}/5)\n")


if correct == 5:
    print("Wow! You did an awesome job!")

elif correct == 3 or correct == 4:
    print("Congratulations! You escaped the room!")

elif incorrect == 3:
    print("I'm sorry, you failed.")

elif incorrect == 5 :
    print("I'm sorry, you suck.")