"""
Module 1 — Lesson 1: List Comprehensions
"""
#Suppose we have a list of numbers and want to create a new list containing only even numbers.
print("-------Even Numbers---------")
numbers = [1, 2, 3, 4, 5, 6]
even=[]
for num in numbers:
    if num%2==0:
        even.append(num)
print(even)



#Create a new list containing only numbers greater than 20 using list comprehension.
numbers = [10, 15, 20, 25, 30, 35, 40]

new=[num for num in numbers if num>20]
print(new)