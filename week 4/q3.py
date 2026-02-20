import math

# Function to calculate effective area of circular flower bed
def effective_area(R, r):
    if R <= r:
        return "Invalid input"
    return math.pi * (R**2 - r**2)
r=int(input("enter the inner radius:"))
R=int(input("enter the outer radius:"))

print("Output =",effective_area(R, r) )
