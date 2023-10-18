'''
Dictionaries and Sets

'''

import json

myDictionary = {'title': 'The Alchemist', 'author': 'Paolo Coelo'}


grade_book = {'Gina': [100, 90, 10], 'Tina': [45, 50, 48], 'Rob': [78, 84, 82]}

num = 1
quit_con = ['quit', 'q']

while True:
    student_name = input("Enter the students name to see their respective grades: ")
    if student_name in quit_con:
        break
    if student_name in grade_book:
        for i in grade_book[student_name]:
            print(f"Grade {num}: {i}")
            num += 1

        grade_change = int(input("Which grade would you like to change: "))
        grade_change = grade_change - 1
        new_value = int(input("Enter the new grade: "))
        new_value = new_value - 1

        for key in grade_book:
            grade_book[student_name][grade_change] = new_value

    else:
        print("That student does not exist")

    with open (r'gradebook.txt','w') as file:
        for key, value in grade_book.items():
            file.write('%s:%s\n' % (key, value))

        file.write(json.dumps(grade_book))

    file.close()


length = len(grade_book)
print(length)