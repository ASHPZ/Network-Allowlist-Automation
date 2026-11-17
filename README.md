# Network Allowlist Automation 🛡️

## Objective

The goal of this project is to create an automated Python algorithm that manages and updates an organization's network access allowlist. This script verifies IP addresses against a specified removal list and securely updates the configuration file to revoke access for unauthorized users.

## Scenario

I am a security professional working at a medical company. As part of my job, I must regularly update a file that identifies employees who can access a restricted subnet containing sensitive personal patient records. Access is strictly controlled based on IP addresses.

There is an `allow_list.txt` file containing the approved IP addresses. Additionally, I am provided with a `remove_list` that identifies employees who have changed roles or left the organization and whose access must be revoked. This project implements a Python script that automates the cross-referencing and removal process, ensuring the network's security perimeter remains intact.

## Python Concepts Applied

* **File Handling:** Using the `with open()` statement for safe resource management in both read (`"r"`) and write (`"w"`) modes.
* **String Manipulation:** Utilizing `.split()` to parse string data into lists, and `.join()` to format list elements back into a string delimited by newlines.
* **Iterative & Conditional Logic:** Employing `for` loops to iterate through data structures and `if` statements to evaluate dynamic conditions.
* **List Mutability:** Modifying list contents dynamically using the `.remove()` method.
* **Modular Programming:** Encapsulating the logic within a reusable, well-documented custom function `update_file()`.

## Algorithm Workflow

1. **Read the File:** Open `allow_list.txt` in read mode and extract its contents as a string.
2. **Convert to List:** Use `.split()` to convert the string of IP addresses into a Python list.
3. **Cross-Reference Data:** Iterate through the provided `remove_list` (rather than the allowlist itself) to avoid index-shifting bugs.
4. **Remove Unauthorized IPs:** For every IP in the removal list, check if it exists in the allowlist. If a match is found, apply `.remove()` to delete it.
5. **Format for Output:** Convert the cleaned list back into a string using `"\n".join()` so that each IP sits on a new line.
6. **Overwrite File:** Open `allow_list.txt` in write mode and replace the old data with the newly updated string.

## Code Snippet

```python
def update_file(import_file, remove_list):
    """
    Updates an allowlist of IP addresses by removing identified IPs.
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
```

## How to Run This Project

1. Clone the repository to your local machine.
2. Ensure you have Python installed (Python 3.x is recommended).
3. Create a file named `allow_list.txt` in the same directory and populate it with sample IP addresses (one per line). Make sure some of those IPs match the ones in the script's `remove_list` parameter.
4. Run the script from your terminal or command prompt:
   `python task.py`
5. Check the terminal output or open `allow_list.txt` to verify that the target IP addresses have been successfully removed.
