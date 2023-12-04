string = '2 Happy 60 To End 7 This 8 Semester 54'

number = []

stripped = string.split()

for i in stripped:
    isnum = i.isdigit()
    if isnum == True:
        number.append(int(i))

    else:
        pass


number.sort(reverse=True)
print(number)

