# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_security.py                             :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/08 11:12:39 by eduaaugu         #+#    #+#              #
#    Updated: 2026/09/08 14:36:09 by eduaaugu        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self._height = height
        self._days = days

    def age(self):
        self._days += 1

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

def ft_age_security(plant: Plant, age: int):
    if plant.set_age(age):
        print(f"Age updated: {plant.get_age()} days")
    else:
        print(f"{plant.name}: Error, age can't be negative")
        print("Age update rejected")

def ft_height_security(plant: Plant, height: int):
    if plant.set_height(height):
        print(f"Height updated: {plant.get_height()}cm")
    else:
        print(f"{plant.name}: Error, height can't be negative")
        print("Height update rejected")

def main():
    rose = Plant("Rose", 15.0, 10)

    print("=== Garden Security System ===")
    print("Plant created:", end=" ")
    rose.show()
    print()
    ft_height_security(rose, 25.0)
    ft_age_security(rose, 30)
    print()
    ft_height_security(rose, -25)
    ft_age_security(rose, -30)
    print()
    print("Current state:", end=" ")
    rose.show()

if __name__ == "__main__":
    main()
