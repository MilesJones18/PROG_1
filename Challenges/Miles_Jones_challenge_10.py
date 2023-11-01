


class PlayerCharacter:
    
    def __init__(self, health, armor_rating, attack_power):
        self.__health = health
        self.__armor_rating = armor_rating
        self.__attack_power = attack_power


    def set_health(self, health):
        self.__health = health

    def get_health(self):
        return self.__health
    

    def set_armor_rating(self, armor_rating):
        self.__armor_rating = armor_rating
    
    def get_armor_rating(self):
        return self.__armor_rating
    

    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power
    
    def get_attack_rating(self):
        return self.__attack_power
    


def main():
    health = 0
    armor_rating = 0
    attack_power = 0

    while int(health) not in range(1,101):
        health = int(input('Please enter your health points (1-100): '))
        if health > 100 or health < 1:
            print('Please enter a value in-between 1-100')

    while int(armor_rating) not in range(1,21):
        armor_rating = int(input('Please enter your armor rating (1-20): '))
        if armor_rating > 20 or armor_rating < 1:
            print('Please enter a value in-between 1-20')

    while int(attack_power) not in range(1,21):
        attack_power = int(input('Please enter your attack power (1-20): '))
        if attack_power > 20 or attack_power < 1:
            print('Please enter a value in-between 1-20')

    wizard = PlayerCharacter(health, armor_rating, attack_power)

    print(f'Health: {wizard.get_health()}\nArmor: {wizard.get_armor_rating()}\nAttack: {wizard.get_attack_rating()}')




if __name__ == '__main__':
    main()