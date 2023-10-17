'''
Parse the Word Frequency.txt file, create a dictionary where each word in the file is a key, and the value is the frequency of each word.
Display the frequency of each word to stdout as a formatted table.

'''


def splitWord():
    word = []
    specificLines = [0, 2]
    with open('Word Frequency.txt','r') as f:
        for pos, l_num in enumerate(f):
            if pos in specificLines:
                content = l_num.replace(', ', ' . ').split()
                for words in content:
                    if words == ',':
                        continue
                    else:
                        word.append(words)
    return word


def addKeys():
    word = splitWord()
    word = list(map(str.lower,word)) # Sets each element to lowercase.
    wordlist = {}  # Dictionary

    for i in word:
        wordlist[i] = wordlist.get(i, 0) + 1
        
    print('Word | Frequency')
    for key, value in wordlist.items():
        print(f'{key}: {value}')


def main():
    addKeys()
    

if __name__ == "__main__":
    main()



