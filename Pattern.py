no = int(input("Enter any range : "))
# half upper part
for i in range(no):
    for j in range(0,no-i-1):
        print(" ",end = "")
    for k in range(0,i+1):
        print("*",end = "")
    print()
# half down part
for i in range(no-1,0,-1):
    for j in range(no,i,-1):
        print(" ",end = "")
    for k in range(i,0,-1):
        print("*",end = "")
    print()