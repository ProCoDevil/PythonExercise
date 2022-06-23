# Print The Reverse Number Pattern
no_of_rows = 5
for i in range (0,no_of_rows + 1) :
    
    for j in range(no_of_rows - i, 0 , -1) :
        print(j, end = '  ')

    print()	