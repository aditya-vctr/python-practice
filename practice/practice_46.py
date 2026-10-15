'''
Write a program to calculate the total cost of a hotel room booking.

The cost depends on the room type, whether it's a weekend, loyalty membership, and payment method.
Room types available:
"standard": Rs: 2000
"deluxe": Rs: 3500
"suite": Rs: 5000
Weekend surcharge: 20% added to the room cost if it's a weekend booking.
Loyalty members get an additional 10% discount on the total cost.
Online payments incur a 3% processing fee on the total cost.
Take the following inputs:
Room type: str
Is weekend: bool: True/False
Is loyalty member: bool: True/False
Is online payment: bool: True/False
Calculate and display the total cost. If the room type is invalid, print "Invalid Room Type" and exit.
'''



room_type = input("Enter your room type: ").lower()
is_weekend = input("Enter True/False for weekend: ") == "True"
is_loyalty_member = input("Enter True/False for loyalty member: ") == "True"
is_online_payment = input("Enter True/False for online payment: ") == "True"

if room_type == "standard":
    cost = 2000
elif room_type == "deluxe":
    cost = 3500
elif room_type == "suite":
    cost = 5000
else:
    print("Invalid Room Type")
    exit()

if is_weekend:
    cost *= 1.2

if is_loyalty_member:
    cost *= 0.9

if is_online_payment:
    cost *= 1.03

print(f"{cost:.2f}")
