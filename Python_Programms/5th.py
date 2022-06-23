#  Complete The Task

# Condition

# 1 - The Number Must Be divisible By Five From The Given List
# 2 - If The Number Is Greter Then 150 , Skip and Move To Other NO
# 3 - The Loop Will Finish at 500

list_items = [12,75,150,100,180,145,525,50]

for item in list_items:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)