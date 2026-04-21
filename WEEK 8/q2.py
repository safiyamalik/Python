n1 = int(input("Enter number of emails in list 1: "))
list1 = []

for i in range(n1):
    email = input("Enter email: ")
    list1.append(email)

n2 = int(input("Enter number of emails in list 2: "))
list2 = []

for i in range(n2):
    email = input("Enter email: ")
    list2.append(email)

union_list = list(set(list1) | set(list2))

print("Master list of unique emails:")
print(union_list)