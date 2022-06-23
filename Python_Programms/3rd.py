# Calculate The Sum Of All Numbers From 1 To Given Numbers

user_no = input("Enter Any Number ")

user_no = int(user_no)

i = 0
count = 0
for i in range(1,user_no + 1):
    count += i

print("Sum of numbers is : ",count)