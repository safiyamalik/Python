list1=list(map(int,input("enter first list:").split()))
list2=list(map(int,input("enter second list:").split()))
merged=list1+list2
merged.sort()
print("sorted list :",merged)
