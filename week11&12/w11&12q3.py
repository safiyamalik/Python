# Employee data
employees = {'Alice': 5001, 'Bob': 5002, 'Charlie': 5003}

# Input Badge ID
badge_id = int(input("Enter Badge ID: "))

# Reverse lookup
found = False

for name, id in employees.items():
    if id == badge_id:
        print("Owner:", name)
        found = True
        break

# If not found
if not found:
    print("ID not found")