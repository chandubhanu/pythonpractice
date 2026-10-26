"""
---------------Type conversion-----------------

Type conversion means changing the variable data type from one type to another
Python has useful conversion tools:
Function	What it does	Example
int()	Converts to an integer	int("26") → 26
float()	Converts to a decimal number	float("2.5") → 2.5
str()	Converts to text	str(26) → "26"
"""


print("---------------Convert str to int-----------------")

num=int(input())
print(num*5)


age=int(input("Enter your age: "))
print(age)
print("Next year, you will be",age+1)