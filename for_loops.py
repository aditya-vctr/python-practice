# for loops = execute a block of code a fixed number of times.
# you can iterate over a range, string, sequence, etc

# for x in reversed(range(1,11)):
#     print(x)

# print("HAPPY BIRTHDAY ADITYA!! 🎂🥳🥳") 


# for x in range(1,11):
#     if x == 3:
#         continue
#     else:
#         print(x)


# countdown timer in python
import time
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}hr :{minutes:02}min :{seconds:02}sec")
    time.sleep(1)
print("HAPPY BIRTHDAY 🎂🥳!! ")