def remove_even_index(s):
    result=""
    for i in range(len(s)):
        if i %2!=0:
            result+=s[i]
    return result
x=input("enter the string:")
print(remove_even_index(x))
    
    
