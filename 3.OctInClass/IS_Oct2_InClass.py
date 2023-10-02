'''
Module 7

Lists and Tuples

'''


#Lists

my_list = [4, 5, 8, 9]  # Indexes are from 0 to N - 1
my_text_list = ['Orange', 'Bananas', 'Fruits']
my_combo_list = ['Orange', 8, 3.45, 'Car']  # Tuples are the same.
my_tuple = (4, 5, 8, 9)

#print(my_combo_list)
# Lists are mutable (changeable), tuples are immutable.

my_list.append(6)
print(my_list)

my_list.insert(2, 10)
print(my_list)

my_list.remove(5)
print(my_list)

my_list.pop(3)
print(my_list)

del my_list[1]
print(my_list)