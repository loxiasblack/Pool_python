#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    list_of_files = [
        "lost_archive.txt",
        "classified_vault.txt",
    ]

    for name_of_file in list_of_files:
        try:
            print(f"CRISIS ALERT: Attempting access to '{name_of_file}'...")
            with open(name_of_file, "r") as file:
                data = file.read()
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")

    file_name = "standard_archive.txt"
    try:
        print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
        with open(file_name, "r") as file:
            data = file.read()
        print(f"SUCCESS: Archive recovered - ``{data}''")
        print("STATUS: Normal operations resumed\n")
    except Exception as e:
        print(f"STATUS: {e}")
    print("All crisis scenarios handled successfully. Archives secure")
