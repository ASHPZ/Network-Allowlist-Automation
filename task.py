def update_file(import_file, remove_list):
    """
    Updates an allowlist of IP addresses by removing identified IPs.
    
    Args:
        import_file (str): The name of the file containing the allowlist.
        remove_list (list): A list of IP addresses to be removed.
    """
    # Read the initial contents of the file
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # Convert the string into a list
    ip_addresses = ip_addresses.split()

    # Iterate through the remove_list to avoid index shifting errors
    for element in remove_list:
        # Evaluate if the element is in the allowlist
        if element in ip_addresses:
            # Remove the unauthorized IP
            ip_addresses.remove(element)

    # Convert the list back to a string with newline separators
    ip_addresses = "\n".join(ip_addresses)

    # Rewrite the file with the updated list
    with open(import_file, "w") as file:
        file.write(ip_addresses)

# Execute the function with the provided sample data
update_file("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])

# Verify the file contents after execution
with open("allow_list.txt", "r") as file:
    text = file.read()

print("Updated file contents:")
print(text)