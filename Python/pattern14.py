n=int(input("enter rows num:"))
for i in range(1, n + 1):
    for j in range(i):
        print(" ", end="")
    #for k in range(2 * n - 1):
        print("*", end="")
    print("")
for i in range(n-1,0,-1):
    for j in range(i):
        print(" ", end="")
    #for k in range(2 * (n-i) + 1):
        print("*", end="")
    print("")