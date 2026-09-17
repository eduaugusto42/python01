def main() -> None:
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.show()
    print()
    ft_height_security(rose, 25)
    ft_age_security(rose, 30)
    print()
    ft_height_security(rose, -25)
    ft_age_security(rose, -30)
    print()
    print("Current state:", end=" ")
    rose.show()


class Plant:
    def __init__(self, name: str, height: float, days: int):
        self.name = name
        self._height = height
        self._days = days

    def age(self) -> None:
        self._days += 1

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
        print(f"{self.name}: "
              f"{round(self._height, 2)}cm, "
              f"{self._days} days old")


def ft_age_security(plant: Plant, age: int) -> None:
    if plant.set_age(age):
        print(f"Age updated: {plant.get_age()} days")
    else:
        print(f"{plant.name}: Error, age can't be negative")
        print("Age update rejected")


def ft_height_security(plant: Plant, height: int) -> None:
    if plant.set_height(height):
        print(f"Height updated: {plant.get_height()}cm")
    else:
        print(f"{plant.name}: Error, height can't be negative")
        print("Height update rejected")


if __name__ == "__main__":
    main()
