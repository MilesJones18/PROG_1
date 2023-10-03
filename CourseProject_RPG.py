'''
4 classes, a superclass called humanoid, followed by 3 classes called Humans, Elves, Dwarves. All three will inherit humanoid, but each will contain there own distinct methods.
'''
import random



class Humanoids:
    def __init__(self):
        self.Race = input("Please choose a race: ")
        if self.Race == '1':
            self.Race = 'Human'
        if self.Race == '2':
            self.Race = 'Elf'
        if self.Race == '3':
            self.Race = 'Dwarf'
        self.Hgt = input(f"Please enter your {self.Race}'s height from 4ft - 7ft: ")
        self.Wgt = input(f"Please enter your {self.Race}'s weight from 60 - 300lbs: ")
        self.Hclr = input(f"Please enter your {self.Race}'s hair color: ")
        self.Eclr = input(f"Please enter your {self.Race}'s eye color: ")
        self.Str = random.randint(1,18)
        self.Dex = random.randint(1,18)
        self.Cons = random.randint(1,18)
        self.Int = random.randint(1,18)
        self.Wis = random.randint(1,18)
        self.Char = random.randint(1,18)


    def displayCurrent(self):
        print(f"\nRace: {self.Race}\nHeight: {self.Hgt} ft\nWeight: {self.Wgt} lbs\nHair Color: {self.Hclr}\nEye color: {self.Eclr}\n")


    def displayStats(self):
        print(f"---Attributes---\nStrength: {self.Str}\nDexterity: {self.Dex}\nConstitution: {self.Cons}\nIntelligence: {self.Int}\nWisdom: {self.Wis}\nCharisma: {self.Char}\n")


class Humans(Humanoids):    
    def HumanStat(self):
        userInput = input("As a human you may add +2 to an attribute of your choice (Enter: strength, dexterity, constitution, etc)")
        if userInput.lower == 'strength':
            self.Str += 2
        if userInput.lower == 'dexterity':
            self.Dex += 2
        if userInput.lower == 'constitution':
            self.Cons += 2
        if userInput.lower == 'intelligence':
            self.Int += 2
        if userInput.lower == 'wisdom':
            self.Wis += 2
        if userInput.lower == 'charisma':
            self.Char += 2


class Elves(Humanoids):
    pass



class Dwarves(Humanoids):
    pass



def characterCreation():
    print(f"Welcome to character creation!\nYou may choose 1 of 3 playable races:\n1. Human\n2. Elf\n3. Dwarf\n")
    character = Humanoids()
    if character.Race == 'Human':
        character = Humans.HumanStat()
    character.displayCurrent()
    character.displayStats()

               




if __name__ == "__main__":
    characterCreation()