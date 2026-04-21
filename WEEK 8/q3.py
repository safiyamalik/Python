n1 = int(input("Enter number of IP addresses in log1: "))
log1 = []

for i in range(n1):
    ip = input("Enter IP address: ")
    log1.append(ip)

n2 = int(input("Enter number of IP addresses in log2: "))
log2 = []

for i in range(n2):
    ip = input("Enter IP address: ")
    log2.append(ip)

common = list(set(log1) & set(log2))

print("Common IP addresses:")
print(common)