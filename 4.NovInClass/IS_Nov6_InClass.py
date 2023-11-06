'''
Recursion

'''

'''
Important facts about recursion

    1. Anything can be solved with recursion can be solved iteratively.

    2. Iteration is usually more efficient; however, the problem could
    be easier to solve with recursion.

    3. Recursion continuosly breaks a problem down into smaller and smaller parts.

    4. A function that calls itself is called a recursive function.

    5. The recursive function must have some means to control the number of times it repeats.

    6. The number of times the function calls itself is called the 'depth of recursion'.

    7. Recursion uses the stack and pushes and pops. This can also cause stack overflows (a
    topic for you to research)


    Complexity Analysis - Big-O Notation
    millisecond = 1/1000 of a second, ms
    microsecond = 1/100,000,000 of a second, us

    
    All recursive algorithms must have the following:

        Base Case: (i.e., when to stop)
        Work toward Base Case (this is where we make the problem simpler)
        Recursive Call (i.e., call ourselves)

        The recursive call is where we use the same algorithm to solve a simpler version
        of the problem.

'''

'''
Example 1: Factorial

base case == the one case where the problem can be solved WITHOUT recursion. Otherwise, we
recursively solve until we hit the base case. 0! is 1 due to the mathematical arrangement
of a data set with no values in it.

'''


def factorial(n):

    
    # base case == 0, because 0! is 1. So this is the only case where the problem
    # an be solved without recursion.
    if n == 0:
        return 1
    
    
    # Recursive case, where we need to keep breaking the problem down into
    # smaller chunks.
    else:
        return n * factorial(n-1)
    

if __name__ == '__main__':
    input = int(input("Please enter a number: "))
    result = factorial(input)
    print(result)    