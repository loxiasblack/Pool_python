#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")
    try:
        file = open("ancient_fragment.txt", "r")
        data = file.read()
        print(f"RECOVERED DATA:\n{data}\n")
        print("Data recovery complete. Storage unit disconnected")
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found")
