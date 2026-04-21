def calculate_routes(n):
    if n==0 or n==1:
        return 1
    else:
        return n*calculate_routes(n-1)
n=int(input("enter the number:"))
print("factorial :", calculate_routes(n))
