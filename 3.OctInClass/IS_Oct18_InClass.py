'''
Dictionaries and Sets, cont.

'''

phonebook = {'John': '511-382-1839', 'Stacy': '321-987-3923', 'Turqouise': '514-563-8414'}
print(phonebook)

phonebook.pop('Turqouise', 'number not found')  # POP removes a single key:value pair.
print(phonebook)


phonebook.popitem()  # Pops the last item in the dictionary.
print(phonebook)


grade_book = {'Gwen': [90, 100, 80], 'Iron Man': [50, 10, 100]}

for val in grade_book.values():
    print(val)


''' Dictionary Comprehesions'''

numbers = [1,2,3,4]

squares = {item:item**2 for item in numbers}  # Start at the for loop.
print(squares)


'''
Sets
'''

mySet = set()
mySet = 'abc'
print(mySet)


myListSet = set([1,2,3,1])

length = len(myListSet)

myListSet.add('a')
print(myListSet)

myListSet.update([9,6,10])
print(myListSet)

myListSet.remove(6)
print(myListSet)

myListSet.clear()  # Removes everything.


# Union of sets
set1 = set([1,5,19,8])
set2 = set([7,6,19,4,1,11])
set3 = set1.union(set2)
print(set3)  # Can use the or operator set3 = set1 | set2


set4 = set1.intersection(set2)
print(set4)  # Can use the and operator set4 = set1 & set2


set5 = set1.difference(set2)
print(set5)


set6 = set1.symmetric_difference(set2)
print(set6)