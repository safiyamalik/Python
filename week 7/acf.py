numbers=list(map(int,input("enter numbers").split()))
result = 0
for i in parser:
    if isinstance(i, int):
        result += i
print("sum of integer values are:", result)
