'''
Person and Customer

Create a class named Person with attributes for a person's name, address, and phone number. Then write a class that is a subclass of 
Person called Customer, should have the attributes for a customer number, and a boolean attribute indicating whether or not the customer
wants to be on the mailing list. Then demonstrate an instance of the Customer class.

'''

class Person():


    ''' Initializes the name, address and phone number data attributes. '''

    def __init__(self, name, address, phone_num):  # Initializes the name, address and phone number data attributes.
        self.__name = name
        self.__address = address
        self.__phone_num = phone_num


    ''' This block sets values to the attributes. '''

    def set_name(self, name): 
        self.__name = name
    
    def set_address(self, address):
        self.__address = address
    
    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num


    ''' This block gets the attributes. '''

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone_num(self):
        return self.__phone_num



class Customer(Person):


    ''' Initializes the customer attributes as well as the inherited person attributes. '''

    def __init__(self, name, address, phone_num, cust_num, mail):  

        Person.__init__(self, name, address, phone_num)

        self.__cust_num = cust_num
        self.__mail = mail

    
    ''' Sets the customer attributes. '''

    def set_cust_num(self, cust_num):
        self.__cust_num = cust_num

    def set_mail(self, mail):
        self.__mail = mail

    
    ''' Gets the customer attributes. '''
    
    def get_cust_num(self):
        return self.__cust_num
    
    def get_mail(self):
        return self.__mail
    


def main():
    
    cust1 = Customer('Miles', '123 Cool Dr', '512-313-5431', 1, False) 
    cust2 = Customer('John', '124 NotCool Rd', '532-546-2133', 2, True)
    cust3 = Customer('Jane', '5612 UTSA Blvd', '210-633-1423', 3, True)

    print('----|Name|----|Address|----|Phone #|----|Customer #|----|Mail|----')
    print(f'     {cust1.get_name()}   {cust1.get_address()}  {cust1.get_phone_num()}       {cust1.get_cust_num()}          {cust1.get_mail()}')
    print(f'     {cust2.get_name()}   {cust2.get_address()}  {cust2.get_phone_num()}     {cust2.get_cust_num()}          {cust2.get_mail()}')
    print(f'     {cust3.get_name()}   {cust3.get_address()}  {cust3.get_phone_num()}     {cust3.get_cust_num()}          {cust3.get_mail()}')




if __name__ == '__main__':
    main()