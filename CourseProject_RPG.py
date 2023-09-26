'''
4 classes, a superclass called humanoid, followed by 3 classes called Humans, Elves, Dwarves. All three will inherit humanoid, but each will contain there own distinct methods.
'''
import random



class Humanoids:
    def __init__(self):
        self.Hgt = input("Please enter your height: ")
        self.Wgt = input("Please enter your weight: ")
        self.Hclr = input("Please enter your hair color: ")
        self.Eclr = input("Please enter your eye color: "),

    def displayCurrent(self):
        print(f"Height: {self.Hgt}\nWeight: {self.Wgt}\nHair Color: {self.Hclr}\nEye color: {self.Eclr}\n")


class Humans(Humanoids):
    pass



class Elves(Humanoids):
    pass



class Dwarves(Humanoids):
    pass



def characterCreation():
    print(f"Welcome to character creation!\n")
    character = Humanoids()
    character.displayCurrent()
               




if __name__ == "__main__":
    characterCreation()