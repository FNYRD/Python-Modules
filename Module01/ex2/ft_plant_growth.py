#!/usr/bin/env python3
class Plant:
    def __init__(self, Name: str, Height: int, Age: int) -> None:
        self.name: str = Name
        self.height: int = Height
        self.plant_age: int = Age
        self.growth_week: int = Height

    def get_info(self) -> None:
        if self.plant_age < 15:
            print(f"\n=== Day {self.plant_age} ===\n"
                  f"Plant's name is: {self.name}\n"
                  f"Its height is: {self.height} centimeters\n"
                  f"It is: {self.plant_age} days old.")
            if self.growth_week != self.height:
                print(f"Growth this week: "
                      f"+{self.height - self.growth_week}cm\n")
                self.growth_week = self.height
        else:
            print("The plant died :c")
        self.growth()
        self.age()

    def growth(self) -> None:
        self.height *= 2

    def age(self) -> None:
        self.plant_age += 7


def main() -> None:
    rosa = Plant("Black Baccara", 30, 1)
    tulip = Plant("Queen of Night", 45, 1)
    cactus = Plant("Saguaro", 15, 1)
    for i in range(3):
        rosa.get_info()
    for i in range(3):
        tulip.get_info()
    for i in range(3):
        cactus.get_info()


if __name__ == "__main__":
    main()
