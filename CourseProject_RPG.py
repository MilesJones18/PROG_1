'''
Welcome to my Character Creator!

There are 3 races Humans, Elves, and Dwarves.
Each have their own attributes.
'''

import random



class Humanoids:
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



class Humans(Humanoids):
    def __init__(self, height, weight, hClr, eClr, str, dex, cons, int, wis, char):
        Humanoids.__init__(self, height, weight, hClr, eClr, str, dex, cons, int, wis, char)

    def humanAtt():
        usrInput = input('Please choose an attribute to +2 too: ').lower()
        if usrInput == 'str':
            Humans.set_str(+2)
        if usrInput == 'dex':
            self.set_dex() + 2
        if usrInput == 'cons':
            self.set_cons() + 2
        if usrInput == 'int':
            self.set_int() + 2
        if usrInput == 'wis':
            self.set_wis() + 2
        if usrInput == 'char':
            self.set_char() + 2


class Elf(Humanoids):
    pass


class Dwarf(Humanoids):
    pass



if __name__ == '__main__':
    race = input('Please choose a race:\n1. Human\n2. Elf\n3. Dwarf\n')
    while True:
        if race == '1':
            player = Humans(height=input('Please enter a height: '),
                            weight=input('Please enter your weight: '),
                            hClr=input('Please enter your hair color: '),
                            eClr=input('Please enter your eclr: '),
                            str=random.randint(1,19),
                            dex=random.randint(1,19),
                            cons=random.randint(1,19),
                            int=random.randint(1,19),
                            wis=random.randint(1,19),
                            char=random.randint(1,19))
            Humans.humanAtt()
            break
        if race == '2':
            player = Elf()
            break
        if race == '3':
            player == Dwarf()
            break
        else:
            print('Please enter a number 1-3')

