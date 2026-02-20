n=int(input("enter the number:"))
if  n<0:
    print("invalid:")
else:
    a=0
    b=1

    while a<n:
        a,b=b,a+b
    if a==n:
        print("fibonacci number:")
    else:
        print("not a fibonacci number:")
