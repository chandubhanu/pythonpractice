orders = [
    {"customer": "John", "product": "Laptop", "price": 50000, "quantity": 1, "status": "delivered"},
    {"customer": "Alice", "product": "Mouse", "price": 500, "quantity": 2, "status": "delivered"},
    {"customer": "John", "product": "Keyboard", "price": 1500, "quantity": 1, "status": "pending"},
    {"customer": "Bob", "product": "Monitor", "price": 12000, "quantity": 2, "status": "delivered"},
    {"customer": "Alice", "product": "Laptop", "price": 50000, "quantity": 1, "status": "delivered"},
    {"customer": "Bob", "product": "Mouse", "price": 500, "quantity": 3, "status": "cancelled"}
]
"""--------------------------NOTE for repeted keys to update the value use customer_spending[customer] += amount"""
"""
Calculate the total revenue from delivered orders only.
Calculate how many delivered orders each customer has.
Calculate the total amount spent by each customer on delivered orders.
Find the customer who spent the most money.
"""
total_revenue=0
delivered_orders={}
customer_spending={}
highest_spending=0
highest_spent_cutomer=''
#Calculate the total revenue from delivered orders only.
for order in orders:
    if order["status"]=='delivered':
        total_revenue+=(order["price"]*order["quantity"])
        customer=order["customer"]
        amount=order['price']* order["quantity"]
        if customer in customer_spending:
            customer_spending[customer]+=amount
        else:
             customer_spending[customer]=amount
        if customer in delivered_orders:
            delivered_orders[customer]+=1
        else:
            delivered_orders[customer]=1
for key,value in customer_spending.items():
    if value>highest_spending:
        highest_spending=value
        highest_spent_cutomer=key
print(total_revenue)
print(delivered_orders)
print(customer_spending)
print(highest_spent_cutomer)
#Calculate how many delivered orders each customer has.

print("------------------------------------------")

customer_spending = {
    "John": 50000,
    "Alice": 51000,
    "Bob": 24000,
    "David": 40000
}
highest=second_highest=0
for key,value in customer_spending.items():
    if value>highest:
        second_highest=highest
        highest=value
    elif value>second_highest and value!=highest:
        second_highest=value

print(second_highest)
