
def compute_average(marks):
    return sum(marks) /len(marks)


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Function to calculate the perimeter of a rectangle
def rectangle_perimeter(length, width):
    return 2 * (length + width)

#average

n=int(input("enter number of subjects:"))
marks=[]
for i in range(n):
    m=float(input("enter marks:"))
    marks.append(m)
avg=compute_average(marks)
print("average of marks =",avg)
#celsius to fahrenheit
celsius=float(input("enter temp in celsius:"))
fahrenheit=celsius_to_fahrenheit(celsius)

print("temperature in fahrenheit=", fahrenheit)
#perimeter
l=float(input("enter length:"))
b=float(input("enter breadth:"))
perimeter=rectangle_perimeter(l,b)
print("perimeter of rectangle ",perimeter)

