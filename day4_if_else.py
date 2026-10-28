"""
What is an if statement?
Imagine a rule:

If it is raining, take an umbrella.
- Is it raining? Yes → Take an umbrella.
- Is it raining? No → You don't need the umbrella because of rain.
Python can follow the same kind of rule.

Keyword	Meaning
if	Check the first condition
elif	Check another condition if earlier ones were false
else	Run when none of the earlier conditions were true
"""

score = 75

if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")