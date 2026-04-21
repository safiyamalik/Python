# Input string from user
text = input("Enter a string: ")

# Create empty dictionary
histogram = {}

# Loop through each character
for char in text:
    if char in histogram:
        histogram[char] += 1
    else:
        histogram[char] = 1

# Print result
print("Character Frequency Histogram:")
print(histogram)