#!/usr/bin/env python3
def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        with open("lost_archive.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix\n"
              "STATUS: Crisis handled, system stable\n")
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        with open("/etc/passwd", "w") as file:
            file.write("test")
    except PermissionError:
        print("RESPONSE: Security protocols deny access\n"
              "STATUS: Crisis handled, security maintained\n")
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as file:
            print(f"SUCCESS: Archive recovered - ``{file.read()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
