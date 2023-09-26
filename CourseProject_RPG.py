'''
4 classes, a superclass called humanoid, followed by 3 classes called Humans, Elves, Dwarves. All three will inherit humanoid, but each will contain there own distinct methods.
'''
import random



class Humanoids:
    def __init__(self, Hgt, Wgt, HClr, EClr, Str, Dex, Cons, Int, Wis, Char):
        self.Hgt = Hgt,
        self.Wgt = Wgt,
        self.Hclr = HClr,
        self.Eclr = EClr,
        self.Str = Str,
        self.Dex = Dex,
        self.Cons = Cons,
        self.Int = Int,
        self.Wis = Wis,
        self.Char = Char,



class Humans:
    pass



class Elves:
    pass



class Dwarves:
    pass



def characterCreation():
    print(f"Welcome to character creation! \n You may choose 1 of 3 races: \n 1.Humans \n 2.Elves \n 3.Dwarves")
    userInput = input("Please choose a race: ")
    if userInput == '1':
        userInput = input("Please enter your height: ")
        userInput = int(input("Please enter your weight: "))
        userInput = input("Please enter your eye color: ")
        userInput = input("Please enter your hair color: ")
               




if __name__ == "__main__":
    characterCreation()