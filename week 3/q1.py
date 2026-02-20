n=int(input("enter the number of prices "))
sum=0
product=1
for i in range(n):
    price=int(input("enter price "))
    sum=sum+price
    product=product*price
average=sum/n
print("sum=", sum)
print("product=", product)
print("average=", average)


 
