r1=int(input("enter first number:"))
r2=int(input("enter second number:"))
if r1<r2:
    numbers=list(range(r1,r2+1))
    print("list of integers:",numbers)
else:
    print("r1 should be less than r2")
