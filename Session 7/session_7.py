# Printing in console / terminal
print("Hello, Python")

# Variables and Data Types
employee_name = "John"
employee_age = 45
print(f"The name of the employee is : {employee_name}")

# List
products = ['Shampoo', 'Conditioner', 'Moisturiser', 'Perfume', 'Shampoo']
products.append('Serum')
print(products)

# Tuple
bestseller = ('Shampoo', 'Conditioner', 'Moisturiser', 'Perfume', 'Shampoo')
print(bestseller)

# Set
recommended = {'Shampoo', 'Conditioner', 'Moisturiser', 'Perfume', 'Shampoo'}
print(recommended)

#Dictionary
product_prices = {
    'Shampoo':100.10,
    'Conditioner':75.27,
    'Moisturiser': 50.00
    
}
print(product_prices)

# Create a dictionary called student_scores with the following key-value pairs:
# "Alice": 85
# "Bob": 90
# "Charlie": 78

student_scores = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}
# Write code to print Bob's score from the student_scores dictionary.
print(student_scores['Bob'])

# Add a new student "Diana" with a score of 92 to the dictionary. Then, update Alice's score to 88.
student_scores['Diana'] = 92
student_scores['Alice'] = 88
print(student_scores)

# Remove Charlie from the dictionary.
del student_scores['Charlie']
print(student_scores)








# Conditional Statements
age = 65

if age>=65:
    print("You are eligible for senior citizen account!")
else:
    print("You are not eligible for senior citizen account!")
    
    
    
# You are designing a simple ticketing system for a movie theater. The ticket prices vary based on the age of the customer and the day of the week. Here are the rules:
# Age-Based Pricing:
# Children (age 12 and under): $5
# Seniors (age 65 and above): $6
# Adults (age 13 to 64): $10
# Day-Based Discounts:
# On weekends (Saturday and Sunday), a discount of $2 is applied to all tickets.
# No discounts are applied on weekdays (Monday to Friday).

# Calculate the final ticket price based on these factors.

ticket_age = 20
base_price = 0.0
weekend_days = ['Saturday', 'Sunday']
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = 'Saturday'
discount = 0.0

if ticket_age<=12:
    base_price = 5.0
elif ticket_age>=65:
    base_price = 6.0
else:
    base_price = 10.0
    
if day in weekend_days:
    discount = 2.0
else:
    discount = 0.0
    
final_price = base_price - discount
    
print(final_price)

# Function
# def function_name():
def square(number):
    return number*number
    
result = square(5)
print(result)