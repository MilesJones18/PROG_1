'''
Welcome to my Character Creator!

There are 3 races Humans, Elves, and Dwarves.
Each have their own attributes.
'''

import random



class Humanoids:  # Sets up the base humanoid class, defines height, weight, eye and hair color, as well as all of the stats.
    def __init__(self, height, weight,
                 hClr, eClr, str,
                 dex, cons, int,
                 wis, char):
        self.__height = height
        self.__weight = weight
        self.__hClr = hClr
        self.__eClr = eClr
        self.__str = str
        self.__dex = dex
        self.__cons = cons
        self.__int = int
        self.__wis = wis
        self.__char = char


    # Set block
    def set_height(self, height: int):
        self.__height = height
    
    def set_weight(self, weight: int):
        self.__weight = weight
    
    def set_hClr(self, hClr: str):
        self.__hClr = hClr
    
    def set_eClr(self, eClr: str):
        self.__eClr = eClr

    def set_str(self, str):
        self.__str = str
    
    def set_dex(self, dex):
        self.__dex = dex
    
    def set_cons(self, cons):
        self.__cons = cons
    
    def set_int(self, int):
        self.__int = int
    
    def set_wis(self, wis):
        self.__wis = wis
    
    def set_char(self, char):
        self.__char = char


    # Get block
    def get_height(self):
        return self.__height
    
    def get_weight(self):
        return self.__weight
    
    def get_hClr(self):
        return self.__hClr
    
    def get_eClr(self):
        return self.__eClr
    
    def get_str(self):
        return self.__str
    
    def get_dex(self):
        return self.__dex
    
    def get_cons(self):
        return self.__cons
    
    def get_int(self):
        return self.__int
    
    def get_wis(self):
        return self.__wis
    
    def get_char(self):
        return self.__char



class Humans(Humanoids):  # Defins the human class, adds a way for the player to choose which stat they want to add 2.
    def __init__(self, height, weight, hClr, eClr, str, dex, cons, int, wis, char):
        Humanoids.__init__(self, height, weight, hClr, eClr, str, dex, cons, int, wis, char)

        strength = self.get_str()
        dexterity = self.get_dex()
        constitution = self.get_cons()
        intelligence = self.get_int()
        wisdom = self.get_wis()
        charisma = self.get_char()

        
        usrInput = input('Please choose a stat to +2 too: ').lower()
        if usrInput == 'str' or 'strength':
            strAdd = strength + 2
            self.set_str(strAdd)
        if usrInput == 'dex' or 'dexterity':
            dexAdd = dexterity + 2
            self.set_dex(dexAdd)
        if usrInput == 'cons' or 'constitution':
            consAdd = constitution + 2
            self.set_cons(consAdd)
        if usrInput == 'int' or 'intelligence':
            intAdd = intelligence + 2
            self.set_int(intAdd)
        if usrInput == 'wis' or 'wisdom':
            wisAdd = wisdom + 2
            self.set_wis(wisAdd)
        if usrInput == 'char' or 'charisma':
            charAdd = charisma + 2
            self.set_wis(charAdd)

class Elf(Humanoids):  # Defines the elf class, a lot simpler than the human class, gets dexterity and charisma and adds 2.
    def __init__(self, height, weight, hClr, eClr, str, dex, cons, int, wis, char):
        Humanoids.__init__(self, height, weight, hClr, eClr, str, dex, cons, int, wis, char)

        dexterity = self.get_dex()
        charisma = self.get_char()

        dexAdd= dexterity + 2
        charAdd = charisma + 2

        self.set_dex(dexAdd)
        self.set_char(charAdd)

class Dwarf(Humanoids):  # Defines the dwarf class, basically the same as the elf class.
    def __init__(self, height, weight, hClr, eClr, str, dex, cons, int, wis, char):
        Humanoids.__init__(self, height, weight, hClr, eClr, str, dex, cons, int, wis, char)

        strength = self.get_str()
        constitution = self.get_cons()
        charisma = self.get_char()

        strAdd = strength + 2
        consAdd = constitution + 2
        charSub = charisma - 2

        self.set_str(strAdd)
        self.set_cons(consAdd)
        self.set_char(charSub)

def menu(player):  # This is just the menu function, just prints out the players attributes.
    print((f'|------Attributes----------|\n'
    '\n'
    f'Height: {player.get_height()}\n'
    f'Weight: {player.get_weight()}\n'
    f'Hair clr: {player.get_hClr()}\n'
    f'Eye clr: {player.get_eClr()}\n'
    '\n'
    f'|---------Stats----------|\n'
    '\n'
    f'Strength: {player.get_str()}\n'
    f'Dexterity: {player.get_dex()}\n'
    f'Constitution: {player.get_cons()}\n'
    f'Intelligence: {player.get_int()}\n'
    f'Wisdom: {player.get_wis()}\n'
    f'Charisma: {player.get_char()}\n'))



if __name__ == '__main__':  # Main function lets the player choose a race, then asks for their physical attributes.
    race = input('Please choose a race:\n1. Human\n2. Elf\n3. Dwarf\n')
    while True:
        if race == '1':
            print('Humans get +2 to any attribute!\n')
            player = Humans(height=input('Please enter a height: '),
                            weight=input('Please enter your weight: '),
                            hClr=input('Please enter your hair color: '),
                            eClr=input('Please enter your eye color: '),
                            str=random.randint(1,19),
                            dex=random.randint(1,19),
                            cons=random.randint(1,19),
                            int=random.randint(1,19),
                            wis=random.randint(1,19),
                            char=random.randint(1,19))
            menu(player)
            break
        if race == '2':
            print(f'Elves get 100% resistance to sleep as well as +2 to dexterity and charisma!\n')
            player = Elf(height=input('Please enter a height: '),
                        weight=input('Please enter your weight: '),
                        hClr=input('Please enter your hair color: '),
                        eClr=input('Please enter your eye color: '),
                        str=random.randint(1,19),
                        dex=random.randint(1,19),
                        cons=random.randint(1,19),
                        int=random.randint(1,19),
                        wis=random.randint(1,19),
                        char=random.randint(1,19))
            menu(player)
            print((f'|--------Special----------|\n'
            '\n'
            f'100% Resistance to sleep (cant be put to sleep)\n'))
            break
        if race == '3':
            print(f'Dwarfs get 20% resistance to magic, +2 to strength and constitution, as well as -2 to charisma\n')
            player = Dwarf(height=input('Please enter a height: '),
                            weight=input('Please enter your weight: '),
                            hClr=input('Please enter your hair color: '),
                            eClr=input('Please enter your eye color: '),
                            str=random.randint(1,19),
                            dex=random.randint(1,19),
                            cons=random.randint(1,19),
                            int=random.randint(1,19),
                            wis=random.randint(1,19),
                            char=random.randint(1,19))
            menu(player)
            print((f'|--------Special----------|\n'
            '\n'
            '20% Resistance to magic\n'))
            break
        else:
            print('Please enter a number 1-3')
            break


