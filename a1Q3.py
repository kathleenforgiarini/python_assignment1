"""
    Topic: Assingment 1 Question 3 - Given a string of odd length greater 7, return a string made of the middle three chars of a given String  
    Date: 17 Sep 2023
    Author: Kathleen
"""

keep_asking = True
while keep_asking:
    string = input('Please enter a string of odd length greater than 7: ')
    length = len(string)

    if (length > 7):
        if (length % 2) == 0:
            print ("String length is not odd")
            keep_asking = True
        else:
            keep_asking = False

            middle_char = length // 2
            middle_three_chars = string[middle_char - 1] + string[middle_char] + string[middle_char + 1] 

            print(middle_three_chars)

    else:
        print("String length less or equal than 7")
        keep_asking = True
