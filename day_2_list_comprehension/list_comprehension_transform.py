"""Lesson 1 — Exercise 2: Transform values"""
#Task: Create a new list containing the square of every number using list comprehension.
numbers = [1, 2, 3, 4, 5]
new=[num*num for num in numbers]
print(new)

#Lesson 1 — Exercise 3: Transformation + condition
"""
Task:
1. Select only even numbers.
2. Calculate the square of each selected number.
3. Store the results in a new list.
Expected output:[4, 16, 36, 64, 100]

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new=[num**2 for num in numbers if num%2==0]
print(new)


#Lesson 1 — Exercise 4: Add an if-else
"""
Now let's learn one important variation.

Suppose we want to create a new list where:
- Even numbers become "Even".
- Odd numbers become "Odd".
Expected output:
"""
numbers = [1, 2, 3, 4, 5]
new=["Even" if num%2==0 else "ODD" for num in numbers]
print(new)


"""
Exercise 5 — Real-world data
Let's apply this to a small QA-style example.
test_results = ["PASS", "FAIL", "PASS", "SKIP", "FAIL", "PASS"]
Create a new list containing only the failed test results, but convert each "FAIL" into "TEST FAILED".
"""


test_results = ["PASS", "FAIL", "PASS", "SKIP", "FAIL", "PASS"]
fail_results=["TEST FAILED"  for res in test_results  if res=="FAIL"]
print(fail_results)