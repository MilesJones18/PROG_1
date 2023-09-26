'''
Write a program that writes a series of random numbers to a file. Each number should be in the range of 1 - 500. Let the user specify how many numbers the file will hold.
Use exception handling to catch an invalid input from the user.
'''
import random


def randomNum(input):
    for i in range(1, input + 1):
        rand = random.randint(1, 500)
        f.write(str(rand) + "\n")


if __name__ == "__main__":
    f = open(r"D:\StudentTestCodeFiles\numbers.txt", "w")  # Change to D:\StudentTestCodeFiles\numbers.txt before turning in.
    while True:
        try:
            userInput = int(input("Please enter the max amount written to the file: "))
            randomNum(userInput)
        except ValueError:
            print("Invalid input, please enter an integer.")
        else:
            break