def is_prime(n):
    if n <= 1:
        return "Not prime"

    for i in range (2,int(n**1/2) +1):
        if n % i == 0:
            return "Not prime"

    return "Prime"
num=int(input("enter the number:"))
print(is_prime(num))
