
n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

print("Original list:", arr)

for i in range(1, n):

    key = arr[i]
    j = i - 1

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key

    print("After iteration", i, ":", arr)

print("Sorted list:", arr)
