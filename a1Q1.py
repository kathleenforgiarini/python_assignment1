"""
    Topic: Assingment 1 Question 1 - Accept two int values from user and return their product. If the product is greater than 1000, then return their sum
    Date: 17 Sep 2023
    Author: Kathleen
"""

first_value = int(input('Please enter a value: '))
second_value = int(input('Please enter another value: '))

product = first_value * second_value
sum = first_value + second_value

if (product > 1000):
    print ("The sum of", first_value, "and", second_value, "is:", sum)
else:
    print ("The product of", first_value, "and", second_value, "is:", product)