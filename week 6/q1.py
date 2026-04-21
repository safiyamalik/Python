a=int(input("enter the first score:"))
b=int(input("enter the second score:"))
c=int(input("enter the third score:"))
highest =a
if b>highest:
    highest =b
if c>highest:
    highest=c
print("highest score is :",highest)
