data = input("Enter a string: ")


words = data.split()


upper_text = data.upper()


index = data.find("rules")


check_char = 'o' in data


sanitized = data.replace("!", "?")

print("Tokens:", words)
print("Uppercase:", upper_text)
print("Index of 'rules':", index)
print("Character 'o' exists:", check_char)
print("Sanitized text:", sanitized)
