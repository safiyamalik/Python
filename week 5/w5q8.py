sentence = input("Enter a sentence: ")

words= sentence.split(" ")

rev_w =[]

for word in words:
    rev_w.append(word[::-1])
result = " ".join(rev_w)
    
print("Output:",result)