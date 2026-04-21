start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

result = []

for x in range(start, end + 1):
    result.append((x, 5*(x**3)))

print("List of tuples:")
print(result)