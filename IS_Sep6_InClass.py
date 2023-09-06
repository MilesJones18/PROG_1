'''

Decision Structures.

if, if-else, elif

'''

#boolean = true/false
#logical operator: and, or, not, !=, ==, >, <, >=, <=

#lower() forces the string into lowercase.

#Truth Tables
'''
AND         OR

TT  = T     TT = T
FF = F      TF = T
FT = F      FT = T
FF = F      FF = F

'''

counter = 0

users_choice = input("Would you like to play a game?: ")

if (users_choice.lower() == "yes" or users_choice.lower() == 'y'):
    print("Hurray!")
    counter += 1  # counter = counter + 1
elif(users_choice.lower() == "no"):
    print("Goodbye")

else:
    print("I don't recognize that response.")
    
print(counter)