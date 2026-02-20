import math
def largest(a,b,c):
    return max(a,b,c)

def volume():
    shape=input("Enter the shape : ")
    if shape=="Cuboid":
       l=float(input("Enter the length: "))
       b=float(input("Enter the breadth: "))
       h=float(input("Enter the height: "))
       return l*b*h
    elif shape=="Cube":
        side=int(input("Enter the side: "))
        return side**3
    elif shape=="Cylinder":
        h=float(input("Enter the height : "))
        r=float(input("Enter the radius: "))
        return  math.pi*(r**2)*h

def areaofrectangle(a,b):
    return a*b

def circumofcircle(r):
    return 2*math.pi*r

def swapping(a,b):
    return b,a

def distbtwpoints(a,b,c,d):
    d=math.sqrt((c-a)**2 + (d-b)**2)
    return d


print("\n-----Data Automation Module------\n")
print("\n1.Largest \n2.Volume \n3.Area of rectangle \n4.Circumference \n5.Swap \n6.Distance between 2 points\n")
choice=input("Enter the choice (1-6): ")

match choice:
    case '1':
        x=int(input("Enter the first number: "))
        y=int(input("Enter the second number: "))
        z=int(input("Enter the third number: "))
        print("Largest: ",largest(x,y,z))

    case '2':
        print("volume: ",volume())

    case '3':
        l=int(input("Enter the length: "))
        b=int(input("Enter the breadth: "))
        print("Area: ",areaofrectangle(l,b))

    case '4':
        r=float(input("Enter the radius:"))
        print("Circumference: ",circuumofcircle(r))

    case '5':
        a=int(input("Enter the first value: "))
        b=int(input("Enter the second value: "))
        print("Swapped: ",swapping(a,b))

    case '6':
         a=int(input("Enter the first value of coordinate 1: "))
         b=int(input("Enter the second value of coordinate 1: "))
         c=int(input("Enter the first value of coordinate 2: "))
         d=int(input("Enter the second value of coordinate 2: "))
         print(distbtwpoints(a,b,c,d))

    case _:
        print("Invalid Choice" )
        

    



    

    
