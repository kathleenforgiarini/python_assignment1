"""
    Topic: Assingment 1 Question 6 - Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
    Date: 17 Sep 2023
    Author: Kathleen
"""

s1 = input('Please enter a string:')
s2 = input('Please enter another string:')

length_s1 = len(s1)
middle_s1 = length_s1 // 2

new_string = s1[:middle_s1] + s2 + s1[middle_s1:]

print(new_string)
