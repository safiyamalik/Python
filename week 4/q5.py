def sum_of_digits(n):
    total = 0
    while n>0:
        total+=n%10
        n//=10
    return total
transaction_id =int(input("enter the id :"))

print("Sum of digits =", sum_of_digits(transaction_id))
