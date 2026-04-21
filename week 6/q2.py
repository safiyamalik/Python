x=float(input("enter the first temperature:"))
y=float(input("enter the second temperature:"))
z=float(input("enter the third temperature:"))
if x<=y and x<=z:
    lowest=x
elif y<=x and y<=z:
    lowest=y
else:
    lowest=z
print("lowest temperature is :",lowest)
    
