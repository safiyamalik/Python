
n = int(input("Enter number of Book IDs: "))

books = []
for i in range(n):
    x = int(input("Enter Book ID: "))
    books.append(x)

key = int(input("Enter Book ID to search: "))

low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if books[mid] == key:
        print("Book ID found at position:", mid)
        found = True
        break

    elif books[mid] < key:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Book ID not found")
