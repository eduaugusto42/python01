def main() -> None:
    plants = {
            "rose": Plant("Rose", 25.0, 30),
            "oak": Plant("Oak", 200.0, 365),
            "cactus": Plant("Cactus", 5.0, 90),
            "sunflower": Plant("Sunflower", 80.0, 45),
            "fern": Plant("Fern", 15.0, 120)
            }
    ft_plant_factory(plants)


class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self.height = height
        self.days = days

    def age(self) -> None:
        self.days += 1

    def grow(self, growth: float) -> None:
        self.height += growth

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.days} days old")


def ft_plant_factory(plants: dict[str, Plant]) -> None:
    print("=== Plant Factory Output ===")
    for plant in plants.values():
        print("Created:", end=" ")
        plant.show()


if __name__ == "__main__":
    main()
