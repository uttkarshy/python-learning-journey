start=int(input("Enter the starting number of the range: "))
end=int(input("Enter the ending number of the range: "))
table=start
while table<=end:
    for i in range(1, 11):
        print(table, "x", i, "=", table*i)
    table+=1
