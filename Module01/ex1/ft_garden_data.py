#!/usr/bin/env python3
class Plant:
    def __init__(self, Name: str, Height: int, Age: int) -> None:
        self.name: str = Name
        self.height: int = Height
        self.age: int = Age

    def __str__(self) -> str:
        print("=== Garden Plant Registry ===")
        return (f"Plant's name is: {self.name}\n"
                f"Its height is: {self.height} centimeters\n"
                f"It is: {self.age} days old.\n")


def main() -> None:
    naranjo = Plant("Naranjo", 300, 30)
    pino = Plant("Pino", 600, 200)
    lavanda = Plant("Lavanda", 25, 3)
    print(naranjo)
    print(pino)
    print(lavanda)


if __name__ == "__main__":
    main()
