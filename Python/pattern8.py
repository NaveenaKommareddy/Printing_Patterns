rows = int(input("Enter Number: "))
for i in range(1, rows + 1):
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print("")
