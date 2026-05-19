#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.water_tank: int = 0
        self.start_height: int = height

    def increase_decrease(self, direction: str) -> None:
        if direction == "+":
            self.height += 1
            print(f"{self.name} grows 1cm")
        elif direction == "-":
            self.height -= 1
            print(f"{self.name} decrease 1cm")

    def testing_wilting(self) -> None:
        if self.height < self.start_height:
            raise PlantError("The tomato plant is wilting!")


class Garden:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.plants: list[Plant] = []
        self.water_tank: int = 100
        self.water_point_break: int = 50

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)

    def quantity_plants(self) -> int:
        return len(self.plants)

    def use_water(self) -> None:
        print("It was used 60 lt of water!")
        self.water_tank -= 60

    def testing_water(self) -> None:
        if self.water_tank < self.water_point_break:
            raise WaterError("Not enough water in the tank!")


class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def detecting_error(self, garden: Garden) -> int:
        return garden.quantity_plants()


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def main() -> None:
    tomato: Plant = Plant("Tomato", 10)
    garden: Garden = Garden("Jesus's Garden")

    tomato.increase_decrease("+")
    tomato.increase_decrease("-")
    tomato.increase_decrease("-")

    garden.use_water()

    print("\nTesting PlantError...")
    try:
        tomato.testing_wilting()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        garden.testing_water()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting GardenError...")
    try:
        tomato.testing_wilting()
    except GardenError as e:
        print(f"Caught a GardenError: {e}")
    try:
        garden.testing_water()
    except GardenError as e:
        print(f"Caught a GardenError: {e}")


if __name__ == "__main__":
    main()
