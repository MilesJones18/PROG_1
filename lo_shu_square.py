'''
The lo shu square has the following properties:
    The grid contains the numbers 1 through 9.
    The sum of each row, column and each diagonal all add up to 15.
'''
import random

COLS = 3
ROWS = 3


def Square():
    values = [[0,0,0],
              [0,0,0],
              [0,0,0],]

    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1,9)


    print(f'{values[0]}\n{values[1]}\n{values[2]}\n')
    return values

def checkSum():
    square = Square()
    diagonal = []
    column = []
    column2 = []
    column3 = []

    for row in square:
        rowSum = row[0] + row[1] + row[2]
        print(f"{rowSum}\n")


    for col in square:
        column.append(col[0])
    print("Column Sum")
    print(column)
    print(sum(column))

    for col in square:
        column2.append(col[1])
    print('Column 2 Sum')
    print(column2)
    print(sum(column2))

    for col in square:
        column3.append(col[2])
    print('Column 3 Sum')
    print(column3)
    print(sum(column3))


    i = 0
    for diag in square:
        diagonal.append(diag[i])
        i += 1
    print("Diagonal Sum")
    print(diagonal)
    print(sum(diagonal))


    diagonal = []
    i = 2
    for diag in square:
        diagonal.append(diag[i])
        i -= 1
    print("Reverse Diagonal Sum")
    print(diagonal)
    print(sum(diagonal))




if __name__ == "__main__":
    checkSum()