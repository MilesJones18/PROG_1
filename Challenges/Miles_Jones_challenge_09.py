'''
Parse the Word Frequency.txt file, create a dictionary where each word in the file is a key, and the value is the frequency of each word.
Display the frequency of each word to stdout as a formatted table.

'''


def splitWord():
    word = []
    specificLines = [0, 2]
    with open('Word Frequency.txt','r') as f:
        for pos, l_num in enumerate(f):  # Enumerates through each line in the file.
            if pos in specificLines:  # Checks if the enumeration is in the specificLines list. 
                content = l_num.replace(', ', ' . ').split()  # Splits each line into words including the period and comma and stores it into the content list.
                for words in content:  # Loops through each word in the content list.
                    if words == ',' or words == '.':  # If the words variable has a period or a comma, pass. Else, append the word to the word list.
                        continue
                    else:
                        word.append(words)
    return word  # This is the final list.


def addKeys():
    word = splitWord()  # Initializes the splitWord() function in the word variable.
    word = list(map(str.lower,word)) # Sets each element to lowercase.
    wordlist = {}  # Initializes an empty dictionary.

    for i in word:  # Loops through each word in the list.
        wordlist[i] = wordlist.get(i, 0) + 1  # Uses the get function to add the word to the dictionary, if the word is already in the list, increment the counter.
        
    print('Word | Frequency')  # Just a clean way to present the data
    for key, value in wordlist.items():
        print(f'{key}: {value}')


def main():
    addKeys()
    

if __name__ == "__main__":
    main()



