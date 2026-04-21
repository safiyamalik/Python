n=int(input("Enter your range: "))
l=[]
for i in range(n):
    p=input("Enter product IDS: ")
    l.append(p)
print(l)
key=input("Enter key to search: ")
if key in l:
    print(key," found")
else:
    print("Not found")
