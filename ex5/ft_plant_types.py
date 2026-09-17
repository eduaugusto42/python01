def main() -> None:
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato.show()
    print("[make the tomato grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    tomato.show()


class Plant:
    def __init__(
            self,
            name: str,
            height: float,
            days: int
            ) -> None:
        self.name = name
        self._height = height
        self._days = days

    def age(self, time: int) -> None:
        self._days += time

    def set_age(self, new_age: int) -> bool:
        if new_age < 0:
            return False
        else:
            self._days = new_age
            return True

    def get_age(self) -> int:
        return self._days

    def grow(self, growth: float) -> None:
        self._height += growth

    def set_height(self, new_height: float) -> bool:
        if new_height < 0:
            return False
        else:
            self._height = new_height
            return True

    def get_height(self) -> float:
        return self._height

    def show(self) -> None:
        print(
                f"{self.name}: {round(self._height, 2)}cm, "
                f"{self._days} days old"
                )


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            color: str
            ) -> None:
        super().__init__(name, height, days)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self.bloomed:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float, days: int,
            trunk_diameter: float
            ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
                f"Tree {self.name} now produces a shade "
                f"of {self._height}cm long "
                f"and {self.trunk_diameter} wide."
                )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            harvest_season: str
            ) -> None:
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def age(self, time: int) -> None:
        super().age(time)
        self.nutritional_value += time

    def grow(self, growth: float) -> None:
        super().grow(growth)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    main()
