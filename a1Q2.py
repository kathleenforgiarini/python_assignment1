"""
    Topic: Assingment 1 Question 2 - Accept five int values from user and return their average. 
    Date: 17 Sep 2023
    Author: Kathleen
"""

print("\nPlease enter 5 int values:")
print("--------------------------")

value_1 = int(input('Value 1: '))
value_2 = int(input('Value 2: '))
value_3 = int(input('Value 3: '))
value_4 = int(input('Value 4: '))
value_5 = int(input('Value 5: '))

sum = value_1 + value_2 + value_3 + value_4 + value_5
average = sum / 5

print ("The avarage of", value_1, ",", value_2, ",", value_3, ",", value_4, "and", value_5, "is", average)
