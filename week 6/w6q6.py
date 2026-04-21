import math
a=float(input("enter first side"))
b=float(input("enter second side"))
c=float(input("enter third side"))
if a+b>c and a+c>b and b+c>a:
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("area of triangle:" ,area)
    if a==b and b==c:
        print("triangle is equilateral")
    elif a==b or b==c or a==c:
        print("triangle is isosceles")
    else:
        print("triangle is scalene")
else:
    print("sides do not form a valid triangle")
