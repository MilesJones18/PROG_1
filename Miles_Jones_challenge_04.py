correct = 0
riddle = 1


game_choice = input("Do you want to play a game? ")


while game_choice.lower() != 'no':


    rid1 =  input("What can you hold in your right hand, but never in your left hand? ")
    if rid1.lower() == "your left hand":
        correct += 1
        print(f"Thats correct! ({correct}/5)\n")
    else:
        print(f"Sorry, thats incorrect. ({correct}/5)\n")
        break
    

    game_choice = input("Do you want to answer another riddle? ")
    if game_choice == 'no':
        print(f"You got {correct} correct.")
        break


    rid2 = input("What gets wet while drying? ")
    if rid2.lower() == "a towel":
        correct += 1
        print(f"Thats correct ({correct}/5)\n")
    else:
        print(f"Sorry, thats incorrect ({correct}/5)\n")
        break


    game_choice = input("Do you want to answer another riddle? ")
    if game_choice == 'no':
        print(f"You got {correct} correct.")
        break

    rid3 = input("What kind of band never plays music? ")
    if rid3.lower() == "a rubber band":
        correct += 1
        print(f"Thats correct! ({correct}/5)\n")
    else:
        print(f"Sorry, thats incorrect. ({correct}/5)\n")
        break


    game_choice = input("Do you want to answer another riddle? ")
    if game_choice == 'no':
        print(f"You got {correct} correct.")
        break

    rid4 = input("What is the end of everything? ")
    if rid4.lower() == "g":
        correct += 1
        print(f"Thats correct! ({correct}/5)\n")
    else:
        print(f"Sorry, thats incorrect ({correct}/5)\n")
        break


    game_choice = input("Do you want to answer another riddle? ")
    if game_choice == 'no':
        print(f"You got {correct} correct.")
        break

    rid5 = input("When is a door no longer a door? ")
    if rid5.lower() == "when it is ajar" or rid5.lower() == "when its ajar":
        correct += 1
        print(f"Thats correct! ({correct}/5)\n")
    else:
        print(f"Sorry, thats incorrect. ({correct}/5)\n")
        break
    
    
    game_choice = input("Do you want to answer another riddle? ")
    if game_choice == 'no':
        print(f"You got {correct} correct.")
        break

        