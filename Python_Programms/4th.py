# Write A Program To Print Multiplication Of Given Number

user_no = input("Enter The Number : ")
user_no = int(user_no)

mul_no = 1
count = 1
ans = 0

while (count <= 10):    
    ans= user_no * mul_no
    print(user_no , "*" , count , "=" , ans)
    
    mul_no += 1
    count += 1