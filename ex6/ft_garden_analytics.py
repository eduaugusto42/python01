class Plant:
    class Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def age(self):
            self._age_count += 1

        def grow(self):
            self._grow_count += 1

        def show(self):
            self._show_count += 1

        def display(self):
            print(f"Stats: {self._grow_count} grow", end=", ") 
            print(f"{self._age_count} age, {self._show_count} show")

    def __init__(self, name, height, days):
        self.name = name
        self._height = height
        self._days = days
        self.stats = Plant.Stats()

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0, 0)

    def age(self, time):
        self._days += time
        self.stats.age()

    def set_age(self, new_age):
        if new_age < 0:
            return False
        else:
            self._days = new_age
            return True
        
    def get_age(self):
        return self._days

    @staticmethod 
    def is_over_year(days):
        return days > 365

    def grow(self, growth):
        self._height += growth
        self.stats.grow()

    def set_height(self, new_height):
        if new_height < 0:
            return False
        else:
            self._height = new_height
            return True

    def get_height(self):
        return self._height

    def show(self):
        print(f"{self.name}: {round(self._height, 2)}cm, {self._days} days old")
        self.stats.show()

class Flower(Plant):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if not self.bloomed:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

class Seed(Flower):
    def __init__(self, name, height, days, color):
        super().__init__(name, height, days, color)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")

class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_count = 0

        def shade(self):
            self._shade_count += 1

        def display(self):
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(self, name, height, days, trunk_diameter):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
        self.stats = Tree.TreeStats()

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of", end =" ")
        print(f"{self._height}cm long and {self.trunk_diameter}cm wide.")
        self.stats.shade()

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

def garden_analytics(plant: Plant):
    plant.stats.display()

def main():
    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    unknown = Plant.create_anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_over_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_over_year(400)}")
    print()
    print("=== Flower")
    rose.show()
    print(f"[statistics for {rose.name}]")
    garden_analytics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    print(f"[statistics for {rose.name}]")
    garden_analytics(rose)
    print()
    print("=== Tree")
    oak.show()
    print(f"[statistics for {oak.name}]")
    garden_analytics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print(f"[statistics for {oak.name}]")
    garden_analytics(oak)
    print()
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print(f"[statistics for {sunflower.name}]")
    garden_analytics(sunflower)
    print()
    print("=== Anonymous")
    unknown.show()
    print(f"[statistics for {unknown.name}]")
    garden_analytics(unknown)


if __name__ == "__main__":
    main()
