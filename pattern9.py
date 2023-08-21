rows = int(input("Enter Number: "))
for i in range(rows,0,-1):
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print("")
