# Initial dictionary
server_config = {"timeout": 300, "status": "active"}

print("=== Read & Inspect ===")

# 1. Print value of "status"
print("Status:", server_config["status"])

# 2. Safely get "admin_email"
print("Admin Email:", server_config.get("admin_email", "Not Set"))

# 3. Total number of settings
print("Total Settings:", len(server_config))

# 4. List of keys and values
print("Keys:", list(server_config.keys()))
print("Values:", list(server_config.values()))

print("\n=== Modify ===")

# 1. Replace "timeout" with its negative
server_config["timeout"] = -server_config["timeout"]

# 2. Add new key-value pair
server_config["max_connections"] = 100

print("Updated Config:", server_config)

print("\n=== Clean Up ===")

# Safely remove "timeout"
removed_value = server_config.pop("timeout", None)
print("Removed 'timeout':", removed_value)

print("Config after removal:", server_config)

print("\n=== Sort ===")

# Print remaining keys in alphabetical order
sorted_keys = sorted(server_config.keys())
print("Sorted Keys:", sorted_keys)
