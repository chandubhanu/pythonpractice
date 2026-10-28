"""
Logical Operators — and, or, and not!

and

Both conditions must be true
Example: Have a ticket AND be old enough.
or

At least one condition must be true
Example: Pay with cash OR a card.

not

Reverses a Boolean value
Example: NOT raining means it isn't raining.
"""

print("------AND------")


age=18
has_voter_id=False

if(age>=18 and has_voter_id):
    print("You can vote")   
else:
    print("You cannot vote")


print("------OR------")

has_cash = False
has_card = False

if has_cash or has_card:
    print("You can pay")
else:
    print("You cannot pay")


print("------NOT------")
is_raining = True
print("Is it raining?", is_raining)
print("Is it not raining?", not is_raining)

is_weekend = True
is_raining = False

if is_weekend and not is_raining:
    print("Go outside")
else:
    print("Stay home")