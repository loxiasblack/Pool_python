#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    with open("classified_data.txt", "r+") as file:
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols\n")

        data = file.read()
        print("SECURE EXTRACTION:")
        print(f"{data}\n")
        print("SECURE PRESERVATION:")
        new_data = "[CLASSIFIED] New security protocols archived"
        print(f"{new_data}")
        file.write(f"\n{new_data}")
        print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")
