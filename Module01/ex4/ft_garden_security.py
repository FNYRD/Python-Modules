#!/usr/bin/env python3
class SecurePlant:
    def __init__(self, Name: str) -> None:
        self.name: str = Name
        self.__height: int = 0
        self.__age: int = 0
        print(f"\nPlant created: {self.name}")

    def set_height(self, height: int) -> None:
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height "
                  f"{self.__height}cm [REJECTED]\n"
                  "Security: Negative height rejected\n")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age "
                  f"{self.__age} days [REJECTED]\n"
                  "Security: Negative or null age rejected\n")

    def get_height(self) -> None:
        if self.__height > 0:
            print(f"Plant {self.name} is {self.__height} cm tall")

    def get_age(self) -> None:
        if self.__age >= 0:
            print(f"Plant {self.name} is {self.__age} days old")


def main():
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Catus")
    plant1.set_age(15)
    plant1.set_height(24)
    plant1.get_age()
    plant1.get_height()

    plant2 = SecurePlant("Rosa")
    plant2.set_age(-5)
    plant2.set_height(0)


if __name__ == "__main__":
    main()
