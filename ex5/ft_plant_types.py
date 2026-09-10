# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/08 15:11:04 by eduaaugu         #+#    #+#              #
#    Updated: 2026/09/10 12:57:25 by eduaaugu        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self._height = height
        self._days = days
    def age(self, time):
        self._days += time
    def set_age(self, new_age):
        if new_age < 0:
            return False
        else:
            self._days = new_age
            return True
    def get_age(self):
        return self._days
    def grow(self, growth):
        self._height += growth
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

class Tree(Plant):
    def __init__(self, name, height, days, trunk_diameter):
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter} wide.")
    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

class Vegetable(Plant):
    def __init__(self, name, height, days, harvest_season):
        super().__init__(name, height, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0
    def age(self, time):
        super().age(time)
        self.nutritional_value += time
    def grow(self, growth):
        super().grow(growth)
    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

def main():
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

if __name__ == "__main__":
    main()
