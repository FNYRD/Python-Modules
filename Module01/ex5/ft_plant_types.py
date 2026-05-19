#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.type: str = "Flower"

    def __str__(self) -> str:
        return (f"{self.name} ({self.type}): {self.height}cm,"
                f" {self.age} days, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter
        self.type: str = "Tree"

    def __str__(self) -> str:
        return (f"{self.name} ({self.type}): {self.height}cm,"
                f" {self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.trunk_diameter * 2}"
              " square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int,
                 age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str | None = None
        self.type: str = "Vegetable"

    def __str__(self) -> str:
        return (f"{self.name} ({self.type}): {self.height}cm,"
                f" {self.age} days, {self.harvest_season} harvest")

    def set_nutritional_value(self, nutritional_value: str) -> None:
        self.nutritional_value = self.name + " " + nutritional_value

    def get_nutritional_value(self) -> None:
        print(self.nutritional_value)


def main() -> None:
    plants: list[Plant] = []
    flowers: list[tuple[str, int, int, str]] = [
        ("Black Baccara Rose", 45, 30, "dark red"),
        ("Ghost Orchid", 20, 15, "white")
    ]

    trees: list[tuple[str, int, int, int]] = [
        ("English Oak", 1500, 3650, 80),
        ("Japanese Cherry", 800, 1825, 40)
    ]

    for name, height, age, color in flowers:
        instance: Flower = Flower(name, height, age, color)
        plants.append(instance)

    for name, height, age, trunk_diameter in trees:
        second_instance: Tree = Tree(name, height, age, trunk_diameter)
        plants.append(second_instance)

    tomato = Vegetable("Cherry Tomato", 60, 45, "summer")
    carrot = Vegetable("Purple Carrot", 30, 60, "autumn")
    tomato.set_nutritional_value("rich in vitamin C and lycopene")
    carrot.set_nutritional_value("high in beta-carotene and fiber")
    plants.append(tomato)
    plants.append(carrot)

    for plant in plants:
        print(plant)
        if isinstance(plant, Flower):
            plant.bloom()
        elif isinstance(plant, Tree):
            plant.produce_shade()
        elif isinstance(plant, Vegetable):
            plant.get_nutritional_value()
        print("\n\n")


if __name__ == "__main__":
    main()
