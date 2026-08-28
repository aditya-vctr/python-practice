'''Define a function named best_diet(filename) that reads this file.
A participant is considered "successful" if their weight strictly decreased every single week
i.e (week1>week2>week3>week4)

The CSV Columns:
ID,Name,Age,Diet_Plan,Week1,Week2,Week3,Week4   '''

def best_diet(filename):
    # 1. create an empty dictionary to act as the scoreboard
    diet_counts= {}
    # 2. open a file in read mode
    f = open(filename,'r')
    # skip the header
    f.readline()
    # 4. loop through the line
    for line in f:
        parts = line.strip().split(',')
        diet = parts[3]
        w1 = int(parts[4])
        w2 = int(parts[5])
        w3 = int(parts[6])
        w4 = int(parts[7])
        #6.check the condition (weight strictly decreasing)
        if w1>w2>w3>w4:
            #7. update the scoreboard
            if diet not in diet_counts:
                diet_counts[diet] = 0
            diet_counts[diet] = diet_counts[diet] + 1
    f.close()

    best_plan = ""
    max_success = -1
    for plan, count in diet_counts.items():
        if count>max_success:
            max_success = count
            best_plan = plan

    return best_plan 