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




class Humans(Humanoids):
    pass



class Elves(Humanoids):
    pass



class Dwarves(Humanoids):
    pass



def characterCreation():
    print(f"Welcome to character creation!")
    Humanoids(Hgt=height,Wgt=weight,HClr=hclr,EClr=eclr)
    height = input("Please enter your height: ")
    weight = int(input("Please enter your weight: "))
    hclr = input("Please enter your eye color: ")
    eclr = input("Please enter your hair color: ")
               




if __name__ == "__main__":
    characterCreation()