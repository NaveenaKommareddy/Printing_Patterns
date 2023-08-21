rows=int(input("enter rows num:"))
columns=int(input("enter columns num:"))
for i in range(1,columns+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")