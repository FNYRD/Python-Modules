#!/usr/bin/env python3
import sys


def main() -> None:
    index: int = 1
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0].split('/')[-1]}")
    if len(sys.argv) == 1:
        print(f"Program name: {sys.argv[0].split('/')[-1]}")
        print(f"Total arguments: {len(sys.argv)}")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for argv in sys.argv:
            if argv == sys.argv[0]:
                pass
            else:
                print(f"Argument {index}: {argv}")
                index += 1
        print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
