'''
Parse the Word Frequency.txt file, create a dictionary where each word in the file is a key, and the value is the frequency of each word.
Display the frequency of each word to stdout as a formatted table.

'''


'''
This function enumerates through each line in the file, it then checks for the lines in the enumerated file.
Next, it splits each word. Finally it loops through each word appending it to the words list, 
not including periods and commas. It returns the list word.
'''
def splitWord():
    word = []
    specificLines = [0, 2]
    with open('Word Frequency.txt','r') as f:
        for pos, l_num in enumerate(f):  
            if pos in specificLines:  
                content = l_num.split()
                for words in content:  
                    word.append(words.strip('.,'))
    return word  



'''
This function initializes the splitWord function and stores it into the variable word and it sets each word to lowercase.
Next, it loops through each word in the list and if the word is in the wordlist dictionary it increases the value for that word,
if it is not in the dictionary, it sets the word as a key and sets the value to 0. Finally, it prints the key:value pair in a table.
'''
def addKeys():
    word = splitWord()  
    word = list(map(str.lower,word)) 
    wordlist = {}  

    for i in word:  
        wordlist[i] = wordlist.get(i, 0) + 1  
        
    print('Word | Frequency')  
    for key, value in wordlist.items():
        print(f'{key}: {value}')


def main():
    addKeys()
    

if __name__ == "__main__":
    main()



