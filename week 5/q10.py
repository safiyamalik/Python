s=input("Enter the string: ")
v_count=0
c_count=0

for ch in s:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        v_count+=1
    else:
        c_count+=1


print("Number of vowels: ",v_count)
print("Number of consonants: ",c_count)
