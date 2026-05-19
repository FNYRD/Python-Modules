#!/usr/bin/env python3
def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    try:
        print("Initializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")
        file.write("[ENTRY 001] New quantum algorithm discovered\n"
                   "[ENTRY 002] Efficiency increased by 347%\n"
                   "[ENTRY 003] Archived by Data Archivist trainee")
        file.close()
        file = open("new_discovery.txt", "r")
        data: str = file.read()
        file.close()
        print(data)
        print("\nData inscription complete. Storage unit sealed.\n"
              "Archive 'new_discovery.txt' ready for long-term preservation.")
    except FileExistsError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
