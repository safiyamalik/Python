a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
while b!=0:
    carry=a&b
    a=a^b
    b=carry<<1
print("sum:", a)
    
            
