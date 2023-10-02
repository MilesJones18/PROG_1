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

this_is_a_list = "I love python!"

length = len(my_list)
print(length)
print(my_combo_list[3])
print(my_combo_list.index('Car'))


my_list = [6, 2, 8, 10, 20, 5, 15,]
my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)


# Gradebook with 10 grades, 0 - 100
# Store grades into a list

grades = []

def gradebook():
    for i in range(0, 10):
        grade = input("Please the first 10 grades (0 - 100): ")
        grades.append(grade)
    return grades


if __name__ == "__main__":
    result = gradebook()
    print(result)