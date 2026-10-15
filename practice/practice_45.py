'''
Write a program to calculate the cost of a meal at a restaurant.
1. The cost of the meal depends on the main dish and the time of the day.
2. Main dishes available:
   - "paneer tikka": ₹250
   - "butter chicken": ₹240
   - "masala dosa": ₹200
3. Additional discounts:
   - 15% discount for meals ordered during luchtime
   (from 12 PM to 3 PM).
4. Customers can apply vouchers for an additional 10% discount on the total  cost.
5. The restaurant accepts card payments.
6. For card payments, there's an additional service charge of 5% on the total cost after applying any discounts.
7. Take the following inputs:
    -Main dish : str
    -Time of the day: int: 24-hour format
    -Whether the customer has a voucher: bool: True/False
    -Whether the payment is by card: bool: True/False
8. Calculate and display the total cost of the meal.

'''

# 🍽️ Restaurant Meal Cost Calculator

# Take and validate main dish
while True:
    main_dish = input("Enter main dish: ").strip().lower()
    if main_dish in ["paneer tikka", "butter chicken", "masala dosa"]:
        break
    print("Invalid dish! Please enter paneer tikka, butter chicken, or masala dosa.")

# Take and validate time
while True:
    try:
        time_of_day = int(input("Enter time (0-23): "))
        if 0 <= time_of_day <= 23:
            break
        print("Invalid time! Enter an hour between 0 and 23.")
    except ValueError:
        print("Invalid input! Please enter a number.")

# Take and validate voucher
while True:
    has_voucher = input("Do you have a voucher? (True/False): ").strip().lower()
    if has_voucher in ["true", "false"]:
        has_voucher = has_voucher == "true"
        break
    print("Invalid input! Enter True or False.")

# Take and validate payment method
while True:
    is_card_payment = input("Pay by card? (True/False): ").strip().lower()
    if is_card_payment in ["true", "false"]:
        is_card_payment = is_card_payment == "true"
        break
    print("Invalid input! Enter True or False.")

# 🍛 Set the price of the main dish
if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200

# 🕛 Apply 15% lunchtime discount (12 PM to 3 PM)
if 12 <= time_of_day <= 15:
    total_cost = cost * 0.85
else:
    total_cost = cost

# 🎟️ Apply an additional 10% voucher discount
if has_voucher:
    total_cost = total_cost * 0.90

# 💳 Apply 5% service charge for card payments
if is_card_payment:
    total_cost = total_cost * 1.05

# 💰 Display the final cost
print(f"Your total bill amount: {total_cost:.2f}")




