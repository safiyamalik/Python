def reverse_string(chars):
    left =0
    right=len(chars)-1

    while left<right:
        chars[left],chars[right]= chars[right],chars[left]
        left+=1
        right-=1


s= input("Enter a string:")

char_list=list(s)

reverse_string(char_list)

print("Reversed string:","".join(char_list))
