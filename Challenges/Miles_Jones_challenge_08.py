'''
Takes a user inputted string, then converts the string to morse code.

Read through each letter, correlate each letter w/ morse code equivalant.
Print out the morse code converted string.

Test: 99 Red Balloons
Expected Result: ----. ----. / .-. . -.. / -... .- .-.. .-.. --- --- -. ...
'''

def conversion(input):
    morseCode = ['--..--','.-.-.-','..--..','-----',
                '.----','..---','...--','....-',
                '.....','-....','--...','---..',
                '----.','.-','-...','-.-.',
                '-..','.','..-.','--.',
                '....','..','.---','-.-',
                '.-..','--','-.','---',
                '.--.','--.-','.-.','...',
                '-','..-','...-','.--',
                '-..-','-.--','--..',' / ']
    
    alphabet = [',','.','?','0',
                '1','2','3','4',
                '5','6','7','8',
                '9','a','b','c',
                'd','e','f','g',
                'h','i','j','k',
                'l','m','n','o',
                'p','q','r','s',
                't','u','v','w',
                'x','y','z',' ']    
    
    converted = []

    for char in input.lower():
        for index, value in zip(alphabet, morseCode):
            if char in index:
                converted.append(value)


    result = ' '.join(converted)
    return result    
            

def main():
    userInput = input("Please enter a string: ")

    result = conversion(userInput)
    print(result)



if __name__ == "__main__":
    main()