#!/usr/bin/env python3
def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    filename: str = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}\n")
    print("Connection established...\n")
    try:
        file = open(filename, "r")
        print("RECOVERED DATA:")
        data: str = file.read()
        print(data)
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
