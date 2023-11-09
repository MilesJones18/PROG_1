'''
Accepts an integer and returns the sum of all the integers from 1 up to the number passed as an argument (1...N)
where N is the number. CAN ONLY USE RECURSION

Test: Use a number less than 100 and greater than 0.
'''


def sumAll(n):
    # This is the base case, if n = 1, return 1.
    if n == 1:
        return 1

    # This is the recursion case, returns n + n-1.
    else:
        return n + sumAll(n-1)


if __name__ == '__main__':
    input = int(input('Please enter a positive number: '))
    result = sumAll(input)
    print(f"Sum: {result}")