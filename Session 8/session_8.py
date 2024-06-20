from functools import reduce

# Functions in Python

# def add(num1, num2):
#     return num1+num2, num1-num2
    
# result = add(10,5)
# print(result)

# Lambda functions
# add = lambda num1,num2: num1+num2
# print(add(15,9))

# Map
# numbers = [2, 3, 4, 5]
# with_tax = list(map(lambda x:x+1, numbers))
# print(with_tax)

# Filter
# numbers = [2,3,4,5,6,7,8,9,10]
# evens = list(filter(lambda x:x%2==0, numbers))
# print(evens)

# Reduce
# numbers = [2,3,4,5,6,7,8,9,10]
# cart_total = reduce(lambda x, y: x+y, numbers)
# print(cart_total)

# Consider the following list of dictionaries representing sales data for a store:
sales_data = [
    {"item": "Laptop", "quantity": 4, "price_per_unit": 1000},
    {"item": "Phone", "quantity": 10, "price_per_unit": 500},
    {"item": "Tablet", "quantity": 5, "price_per_unit": 300},
    {"item": "Monitor", "quantity": 3, "price_per_unit": 150},
    {"item": "Keyboard", "quantity": 7, "price_per_unit": 50},
    {"item": "Mouse", "quantity": 8, "price_per_unit": 25},
    {"item": "Charger", "quantity": 15, "price_per_unit": 20},
    {"item": "Headphones", "quantity": 6, "price_per_unit": 80},
]

# Calculate Total Sales for Each Item: Use map to create a new list of dictionaries where each dictionary contains the item name and the total sales (quantity * price_per_unit) for that item.
total_sales = list(map(lambda x:{"item":x["item"], "total_sales":x["quantity"]*x["price_per_unit"]}, sales_data))
print(total_sales)

# Filter High Sales Items: Use filter to create a list of items where the total sales are greater than $1000.
high_sales_filter = list(filter(lambda x: x["total_sales"]>1000, total_sales))
# print(high_sales_filter)

# Calculate Total Revenue: Use reduce to calculate the total revenue from all the items.
total_revenue = reduce(lambda acc, x:acc + x["total_sales"], total_sales, 0)
print(total_revenue)













