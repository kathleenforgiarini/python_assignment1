"""
    Topic: Assingment 1 Question 4 - Given a string and an int n, remove characters from string starting from zero upto n and return a new string
    Date: 17 Sep 2023
    Author: Kathleen
"""

string = input('Please enter a string: ')
value = int(input('Please enter an integer value: '))

if len(string) == value:
    string = ""

elif len(string) < value:
    string = ""
    
else:

    for i in range(value-1, -1, -1): 
        string = string.replace(string[i],"") 

print ("The final string is: ", string)


