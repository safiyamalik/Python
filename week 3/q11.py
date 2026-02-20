n=int(input("enter the number:"))
if  n<=1:
    print(n, "is not a prime number")
else:
    x=int((n**(1/2))+1)
    for i in range(2,x):
        if n%i==0:
          print(n,"is not prime")
          print("first factor",i)
          break
        else:
            print(n,"is a prime ")
    
    
