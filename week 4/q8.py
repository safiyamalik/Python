def count_case(text):
    upper_count = 0
    lower_count = 0

    for ch in text:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1

    return upper_count, lower_count
text1 =input("enter the text:")
u1, l1 = count_case(text1)
print("Uppercase =", u1, ", Lowercase =", l1)
