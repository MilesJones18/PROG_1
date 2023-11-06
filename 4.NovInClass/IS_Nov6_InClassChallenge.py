

def recursive_line(n):
    
    if n == 1:
        return '*'
    
    else:
        return *recursive_line(n-1), (n*'*')  # *recursive_line is unpacked.


if __name__ == '__main__':
    input = int(input('Please enter a positive number: '))
    result = recursive_line(input)
    for items in result:
        print(items)