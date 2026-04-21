# Input two lists
list1 = list(map(int, input("Enter first list of product IDs: ").split()))
list2 = list(map(int, input("Enter second list of product IDs: ").split()))

# Merge the lists
merged_list = list1 + list2

# Sort the merged list
merged_list.sort()

# Display result
print("Final sorted list:", merged_list)
       
