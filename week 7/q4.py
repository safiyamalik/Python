def find_signal(a,b):
    if b==0:
        return a
    else:
        return find_signal(b,a%b)
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("GCD:", find_signal(a,b))
