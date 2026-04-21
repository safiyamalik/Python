num=int(input("enter a number:"))
temp=num
sum=0

digits=len(str(num))
while temp>0:
    digit=temp%10
    sum+=digit**digits
    temp=temp//10
if sum==num:
    print("armstrong number")
else:
    print("not an armstrong number")
    

