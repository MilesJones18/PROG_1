my_new_int, my_fav_color = 5, "purple"  # Multiple declartions on one line.
my_float = 4.999


print(my_float, "\n")  # Prints on a new line.
print(int(my_float), "\n")  # Since it is caste as an integer, it strips the decimal off of the variable.

#Input is a string/character, you can convert it to another caste by initializing a new variable as an integer/float etc.


#Variable reassignment.
my_float = 4.74
print(my_float, "\n")


GRAVITY = 9.81  # This is a constant variable.


my_int = 5
print(my_int**2)  # Squared
print(my_float / 2)  # Floating point division.
print(my_float // 2)  # Integer division.

print(my_int % 2)  # Modulus (Remainder


'''
Formatting Output
'''

#Using quotation marks in the print statement.
print(""" "To be or not to be. That is the question" """)


my_float_1 = 10.0
my_float_2 = 3.0

print(f"10 / 3 rounded is: {my_float_1 / my_float_2}")

result = my_float_1 / my_float_2   
print(f"10 / 3 rounded to 3 decimal places is: {result:.3f}")