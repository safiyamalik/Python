def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]    
    return quick_sort(left) + middle + quick_sort(right)
n = int(input("Enter number of log entries: "))
logs = []
for i in range(n):
    value = int(input("Enter log value: "))
    logs.append(value)
sorted_logs = quick_sort(logs)
print("Sorted log file:")
print(sorted_logs)
