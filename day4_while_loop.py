"""
---------While loop---------

What is a loop?
Imagine you need to say “Hello” five times.

Without a loop, you might write:
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

Short revision summary
- while loop: Repeats code while a condition is True.
- Condition: Python checks it before every repetition.
- Updating a variable: i = i + 1 increases i by 1; i = i + 2 increases it by 2.
- Stopping: When the condition becomes False, the loop ends.
- Infinite loop: If the variable never changes and the condition stays True, the loop may run forever.
Remember this
Think of a while loop like climbing stairs. You keep climbing while you haven't reached the last step. You must move forward to reach the end!
"""

i=1

while i<=5:
 print("Hello")
 i+=1
