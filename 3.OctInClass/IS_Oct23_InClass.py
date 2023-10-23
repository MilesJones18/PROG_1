'''
Classes/OOP

'''

# Every method must have the self parameter.

import math

class Circle:
    '''
    Class attributes go here, as in the __init__ for initialization.
    Self is mandatory in every method. Self ensures Python is operating on the specific object
    that the method is supposed to operate on.
    '''
    def __init__(self, radius):
        self.__radius = radius  # __radius is a private variable
    

    #accessors and mutators
    def set_radius(self, radius):  # Sets the value
        self.__radius = radius

    def get_radius(self):  # Gets the value
        return self.__radius
    

    #methods go here
    def area(self):
        return math.pi * self.__radius**2
    
    def circumference(self):
        return 2 * self.__radius * math.pi
    
    def diameter(self):
        return 2 * self.__radius
    

def main():
    circle_radius = float(input('Enter the radius for the circle: '))
    
    my_circle = Circle(circle_radius)  # Creating a new object called my_circle

    area = my_circle.area()
    circumference  = my_circle.circumference()
    diameter = my_circle.diameter()

    print(f"The area of the circle is {area}, with a radius of {my_circle.get_radius()}, a cicumference of {circumference}, and a diameter of {diameter}")
    
if __name__ == "__main__":
    main()