# Program To Count Total Number From Given Input

user_no = int(input("Enter Number : "))

total_no = 0

while(user_no>0):
    total_no += 1
    user_no = user_no//10
    
print("Total Number",total_no)