correct = 0

game_choice = input("Do you want to play a game? ")


while game_choice.lower() != 'no':
        
        rid1 =  input("What can you hold in your right hand, but never in your left hand? ")
        if rid1.lower() == "your left hand":
            correct += 1
            print(f"Thats correct! ({correct}/5)\n")
        else:
            print(f"Sorry, thats incorrect You were asked {correct}/5 and you answered ({correct}/5) correct.\n")
            second_choice = input("Do you want to try again? ")
            if second_choice.lower() == "yes":
                continue
            else:
                break


        rid2 = input("What gets wet while drying? ")
        if rid2.lower() == "a towel":
            correct += 1
            print(f"Thats correct ({correct}/5)\n")
        else:
            print(f"Sorry, thats incorrect, You were asked {correct}/5 and you answered ({correct}/5) correct.\n")
            second_choice = input("Do you want to try again? ")
            if second_choice.lower() == "yes":
                continue
            else:
                break


        rid3 = input("What kind of band never plays music? ")
        if rid3.lower() == "a rubber band":
            correct += 1
            print(f"Thats correct! ({correct}/5)\n")
        else:
            print(f"Sorry, thats incorrect, You were asked {correct}/5 and you answered ({correct}/5) correct.\n")
            second_choice = input("Do you want to try again? ")
            if second_choice.lower() == "yes":
                continue
            else:
                break


        rid4 = input("What is the end of everything? ")
        if rid4.lower() == "g":
            correct += 1
            print(f"Thats correct! ({correct}/5)\n")
        else:
            print(f"Sorry, thats incorrect, You were asked {correct}/5 and you answered ({correct}/5) correct.\n")
            second_choice = input("Do you want to try again? ")
            if second_choice.lower() == "yes":
                continue
            else:
                break


        rid5 = input("When is a door no longer a door? ")
        if rid5.lower() == "when it is ajar" or rid5.lower() == "when its ajar":
            correct += 1
            print(f"Thats correct! ({correct}/5)\n")
        else:
            print(f"Sorry, thats incorrect, You were asked {correct}/5 and you answered ({correct}/5) correct.\n")
            second_choice = input("Do you want to try again? ")
            if second_choice.lower() == "yes":
                continue
            else:
                break
        
        print(f"Congratulations! You got all the riddles correct!")
        break

        