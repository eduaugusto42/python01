def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    ft_plant_growth(rose, 0.8)


class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def age(self) -> None:
        self.days += 1

    def grow(self, growth: float | int) -> None:
        self.height += growth

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.days} days old")


def ft_plant_growth(plant: Plant, growth: float | int) -> None:
    initial_height = plant.height

    print("=== Garden Plant Growth ===")
    plant.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.age()
        plant.grow(growth)
        plant.show()
    print(f"Growth this week: {round(plant.height - initial_height, 2)}cm")


if __name__ == "__main__":
    main()
