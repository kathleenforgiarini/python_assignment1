"""
    Topic: Assingment 1 Question 9 - Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list 
    Date: 17 Sep 2023
    Author: Kathleen
"""

list = [54, 44, 27, 79, 91, 41]
list_length = len(list)

removed_number = list.pop(4)

list.insert(1,removed_number)
list.append(removed_number)

print (list)
