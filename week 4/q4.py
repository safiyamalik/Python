def factorial(n):
    if n < 0:
        return "Invalid input"
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


num= int(input("enter the number:"))
print("Factorial =", factorial(num))
