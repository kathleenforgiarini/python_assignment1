"""
    Topic: Assingment 1 Question 7 - Find all occurrences of “USA” in given string (uppercase and lowercase). Welcome to USA. usa awesome, isn't it? 
    Date: 17 Sep 2023
    Author: Kathleen
"""

string = "Welcome to USA. usa awesomen, ins't it?"

string_lowercase = string.lower()
usa_count = string_lowercase.count("usa") 

print ("The word 'usa' appeared", usa_count, "times in the string:", string)
