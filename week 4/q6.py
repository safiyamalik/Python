def is_perfect_number(n):
    if n <= 1:
        return "Not a perfect number"

    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i

    if divisor_sum == n:
        return "Perfect number"
    else:
        return "Not a perfect number"
    
num=int(input("enter  the number:"))
print(is_perfect_number(num))
