#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...\n")
    file = open("new_discovery.txt", "w")
    print("Inscribing preservation data...")
    tuple_of_archive = (
        "[ENTRY 001]: New quantum algorithm discovered\n",
        "[ENTRY 002]: Efficiency increased by 347%\n",
        "[ENTRY 003]: Archived by Data Archivist trainee\n"
    )
    for data in tuple_of_archive:
        print(data)
        file.write(f"{data}")
    file.close()
    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
