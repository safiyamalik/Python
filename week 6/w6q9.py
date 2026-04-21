numbers=list(map(int,input("enter numbers").split()))
numbers.sort()
is_consecutive=True
for i in range(len(numbers)-1):
    if numbers[i]+1!=numbers[i+1]:
        is_consecutive=False
        break
if is_consecutive:
    print("numbers are consecutive")
else:
    print("numbers are not consecutive")
