#nested for

rows=int(input("enter number of rows: "))
columns=int(input("enter number of columns: "))
symbol=input("enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print("")
