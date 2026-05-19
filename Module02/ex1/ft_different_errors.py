#!/usr/bin/env python3
from io import TextIOWrapper


def garden_operations() -> None:
    int("error")

    division: int = 222 // 0
    division = division

    file: TextIOWrapper = open("missing.txt", "r")
    file.read()
    file.close()

    garden: dict[str, int] = {"Flowers": 3, "Trees": 5}
    plants: int = garden["plant"]
    plants = plants


def test_error_teypes() -> None:
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        int("error")
    except ValueError:
        print("Caught ValueError: Invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        division: int = 300 // 0
        division = division
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        file: TextIOWrapper = open("file.txt", "r")
        file.read()
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    print("Testing KeyError...")
    try:
        garden: dict[str, int] = {"Flowers": 3, "Trees": 5}
        plants: int = garden["plant"]
        plants = plants
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


def main() -> None:
    test_error_teypes()


if __name__ == "__main__":
    main()
