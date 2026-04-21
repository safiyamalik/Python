n = int(input("Enter number of filenames: "))

files = []
for i in range(n):
    name = input("Enter filename: ")
    files.append(name)

sorted_files = sorted(files, key=len)

print("Sorted filenames based on length:")
print(sorted_files)
