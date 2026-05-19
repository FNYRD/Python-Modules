#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    print("Input Stream active. Enter archivist ID: ", end="", flush=True)
    id_archivist: str = sys.stdin.readline().strip()
    report: str = input("Input Stream active. Enter status report: ")
    sys.stdout.write(
        f"\n[STANDARD] Archive status from {id_archivist}: {report}"
    )
    sys.stderr.write("\n[ALERT] System diagnostic: Communication channels "
                     "need verification!")
    sys.stdout.write("\n[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
