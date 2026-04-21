nums=list(map(int,input("enter numbers :").split()))
even_ids=[]
odd_ids=[]
for i in nums:
    if i%2==0:
        even_ids.append(i)
    else:
        odd_ids.append(i)
print("even ids (low priority):", even_ids)
print("odd_ids(high_priority):", odd_ids)
