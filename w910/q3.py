ss=[]
n=int(input("Enter your range: "))
for i in range(n):
    s=input("Enter the songs: ")
    ss.append(s)
    
print("Before sorting: \n")
print(ss,"(\n)")
ss.sort()
print("After sorting: \n")
print(ss,"(\n)")
