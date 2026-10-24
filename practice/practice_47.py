'''
Question 1: The Positive Calculator (Using continue)
You have a list of bank account transactions, both deposits (positive) and withdrawals (negative). 
Write a loop that calculates the total amount of deposits only. You must use continue to skip the withdrawals.
'''
transactions = [50, -20, 100, -10, 30]
total_deposits = 0

for amount in transactions:
    # If the transaction is a withdrawal (less than 0), skip it
    if amount < 0:
        continue
        
    # This line only runs if the continue was NOT triggered
    total_deposits += amount

print(total_deposits) # Output will be 180

'''
Question 2: The Needle in the Haystack (Using break)
You are writing a security scanner that checks a list of files for a virus named "trojan.exe". 
If it finds the virus, it should print "Threat found!" and immediately stop scanning to quarantine the system.
'''
files = ["system.dll", "game.exe", "trojan.exe", "notes.txt", "photo.jpg"]

for file in files:
    if file == "trojan.exe":
        print("Threat found! Stopping scan.")
        break # Emergency exit!
        
    # This line only prints if we haven't hit the break
    print(f"{file} is safe.")

'''
Question 3: The Factory Line (Using both)
A conveyor belt is moving items. If an item is "Empty", the belt should just skip it. 
If an item is a "Rock", the machine will break, so the belt must stop completely. Otherwise, it should print that it is processing the item.
'''
conveyor_belt = ["Apple", "Empty", "Banana", "Rock", "Orange"]

for item in conveyor_belt:
    # Rule 1: Skip empty spaces
    if item == "Empty":
        continue
        
    # Rule 2: Emergency stop for rocks
    if item == "Rock":
        print("Rock detected. Halting belt!")
        break
        
    # Rule 3: Process standard items
    print("Processing:", item)