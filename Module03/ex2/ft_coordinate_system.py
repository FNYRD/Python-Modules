#!/usr/bin/env python3
import sys
import math


def calculating_distance(pos1: tuple[int, int, int],
                         pos2: tuple[int, int, int]) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


def parser(position: str) -> tuple[int, int, int]:
    parsed: list[str] = position.split(',')
    x: int = int(parsed[0])
    y: int = int(parsed[1])
    z: int = int(parsed[2])
    return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    pos0: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created:{pos0}")
    pos1: tuple[int, int, int] = (0, 0, 0)
    distance1: float = calculating_distance(pos0, pos1)
    print(f"Distance between {pos0} and {pos1}: {distance1:.2f}\n")
    position: str = "3,4,0"
    print(f"Parsing coordinates: {position}")
    pos2: tuple[int, int, int] = parser(position)
    print(f"Parsed position: {pos2}")
    distance2: float = calculating_distance(pos1, pos2)
    print(f"Distance between {pos1} and {pos2}: {distance2:.2f}")
    if len(sys.argv) == 2:
        arg: str = sys.argv[1]
        print(f"\nParsing coordinates: \"{arg}\"")
        try:
            pos3: tuple[int, int, int] = parser(arg)
            print(f"Parsed position: {pos3}")
            distance3: float = calculating_distance(pos1, pos3)
            print(f"Distance between {pos1} and {pos3}: {distance3}")
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    elif len(sys.argv) > 2:
        print("\nToo many arguments")
    else:
        print("\nArguments empty")

    print("\nUnpacking demonstration:")
    x, y, z = pos0
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
