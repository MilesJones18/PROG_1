'''
Fizz-Buzz

Prints fizz if a number is divisible by 3.
Prints fuzz if a number is divisible by 5.
Prints fizzbuzz if a number is divisible by 3 and 5.
'''

def isDivisible():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} fizzbuzz")
            continue
        if i % 3 == 0:
            print(f"{i} fizz")
        if i % 5 == 0:
            print(f"{i} fuzz")
        else:
            print(i)
        


if __name__ == "__main__":
    isDivisible()