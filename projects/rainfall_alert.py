# Rainfall Alert 
'''
Write a function rainfall_alert(rainfall: list) -> str that takes a list of rainfall values
and returns an alert according to the followin rules:
1. If the list is empty, return "No Rainfall Data"
2. If any rainfall value is above 200, return "Flood Alert" 
3. If all rainfall values are 0, return "Dry week"
4. Otherwise, return "Normal Rainfall".
'''
def rainfall_alert(rainfall: list) -> str:
    # Check if the list is empty
    if rainfall == []:
        return "No Rainfall Data"

    # Check if any value is above 200
    for x in rainfall:
        if x > 200:
            return "Flood Alert"

    # Check if all values are 0
    for x in rainfall:
        if x != 0:
            return "Normal Rainfall"
    return "Dry Week"

print(rainfall_alert([0,0,0,0,0,0,0]))  # Dry week
print(rainfall_alert([])) # No Rainfall Data
print(rainfall_alert([50,100,250,80])) # Flood Alert
print(rainfall_alert([20,50,100,80])) # Normal Rainfall