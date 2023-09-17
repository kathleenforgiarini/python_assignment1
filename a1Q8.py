"""
    Topic: Assingment 1 Question 8 - Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second. 
    Date: 17 Sep 2023
    Author: Kathleen
"""

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

print ("List one: ", listOne)
print ("List two: ", listTwo)

listOne_length = len(listOne)
listTwo_length = len(listTwo)

listThree = []

for i in range (listOne_length):
    if (i % 2) == 1:
        listThree.append(listOne[i])

for i in range (listTwo_length):
    if (i % 2) == 0 :
        listThree.append(listTwo[i])

print (listThree)
    
