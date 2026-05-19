#!/usr/bin/env python3
# Parent class


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        if self.check_len(height):
            self.height: int = height
            print("Height validation test: True")
        else:
            self.height = 0
            print(
                "You provided a negative number, "
                "by default height it'll be == 0"
            )

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm"

    # Method that allows growing the plants by 1cm
    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    @staticmethod
    def check_len(height: int) -> bool:
        return height > 0


class FloweringPlant(Plant):
    def __init__(
        self, name: str, height: int, color: str
    ) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.is_blooming: bool = False

    # This function changes the is_blooming boolean to True
    def bloom(self) -> None:
        self.is_blooming = True

    def __str__(self) -> str:
        # I've called bloom to replicate correctly the subject's example
        self.bloom()
        if self.is_blooming:
            return (
                f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming)"
            )
        else:
            return f"{self.name}: {self.height}cm"


# Class for prized flowers just adding the attribute prize_points
class PrizeFlower(FloweringPlant):
    def __init__(
        self, name: str, height: int, color: str
    ) -> None:
        super().__init__(name, height, color)
        self.prize_points: int = self.calculating_points()

    def __str__(self) -> str:
        return (
            super().__str__()
            + f" Prize points: {self.prize_points}"
        )

    def calculating_points(self) -> int:
        return self.height // 5


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.grow_times: int = 0

    def add_plant(self, plant: Plant) -> None:
        print(f"Added {plant.name} to {self.owner}'s garden")
        self.plants.append(plant)

    def grow_all(self) -> None:
        print(
            f"\n{self.owner} is helping all plants grow..."
        )
        self.grow_times += 1
        for plant in self.plants:
            plant.grow()


class GardenManager:
    class GardenStats:
        def __init__(self) -> None:
            self.garden_list: list[Garden] = []

        def add_garden_stats(self, garden: Garden) -> None:
            self.garden_list.append(garden)

        # Show how many of each kind of plant there are
        def show_types(self) -> None:
            for garden in self.garden_list:
                regular: int = 0
                flowering: int = 0
                prize_flower: int = 0
                for plant in garden.plants:
                    name = plant.__class__.__name__
                    if name == "PrizeFlower":
                        prize_flower += 1
                    elif name == "FloweringPlant":
                        flowering += 1
                    elif name == "Plant":
                        regular += 1
            print(
                f"Plant types: {regular} regular, "
                f"{flowering} flowering, "
                f"{prize_flower} prize flowers"
            )

        # Shows the scores of all of the managed gardens
        def show_scores(self) -> None:
            flag: int = 0
            for garden in self.garden_list:
                flag += 1
                height: int = 0
                prized: int = 0
                score: int = 0
                for plant in garden.plants:
                    height += plant.height
                    cls = plant.__class__.__name__
                    if cls == "PrizeFlower":
                        prized += (
                            plant.prize_points  # type: ignore[attr-defined]
                            * 4
                        )
                score = prized + height
                if flag == 1:
                    print(
                        f"Garden scores - "
                        f"{garden.owner}: {score}",
                        end="",
                    )
                else:
                    print(f", {garden.owner}: {score}")
            if flag == 1:
                print("\n")

        @staticmethod
        def lenght(garden: Garden) -> int:
            quantity: int = 0
            for plants in garden.plants:
                quantity += 1
            return quantity

        # Report each plant and general stats about them
        def report_by_garden(
            self, garden: Garden, owner: str
        ) -> None:
            if garden.owner == owner:
                print(
                    f"\n=== {garden.owner}'s "
                    f"Garden Report ==="
                )
                print("Plants in garden: ")
                for plant in garden.plants:
                    print(" -", end=" ")
                    print(plant)
                length = self.lenght(garden)
                total = garden.grow_times * length
                print(
                    f"\nPlants added: {length}, "
                    f"Total growth: {total}"
                )
                self.show_types()

    def __init__(self) -> None:
        self.gardens: list[Garden] = []
        self.stats: GardenManager.GardenStats = (
            GardenManager.GardenStats()
        )

    @classmethod
    def create_garden_network(cls) -> 'GardenManager':
        return cls()

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)
        self.stats.add_garden_stats(garden)
        print(f"Added {garden.owner} to the Garden Manager")

    # Call for each garden the general stats
    def show_info(self, owner: str) -> None:
        for garden in self.gardens:
            if garden.owner == owner:
                self.stats.report_by_garden(garden, owner)

    # Summarize the scores
    def general_scores(self) -> None:
        self.stats.show_scores()

    def total_gardens(self) -> None:
        quantity: int = 0
        for garden in self.gardens:
            quantity += 1
        print(f"Total gardens managed: {quantity}")


def main() -> None:
    print("=== Garden Management System Demo ===")
    plants_alice: list[Plant] = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow"),
    ]
    alice_garden: Garden = Garden("Alice")
    for plant in plants_alice:
        alice_garden.add_plant(plant)
    alice_garden.grow_all()

    plants_bob: list[Plant] = [
        Plant("Oak Tree", 1),
        FloweringPlant("Rose", 1, "red"),
        PrizeFlower("Sunflower", 50, "yellow"),
    ]
    bob_garden: Garden = Garden("Bob")
    for plant in plants_bob:
        bob_garden.add_plant(plant)

    manager: GardenManager = GardenManager.create_garden_network()
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    manager.show_info("Alice")
    manager.general_scores()
    manager.total_gardens()


if __name__ == "__main__":
    main()
