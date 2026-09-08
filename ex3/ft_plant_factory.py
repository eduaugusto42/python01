# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_factory.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/03 17:58:12 by eduaaugu         #+#    #+#              #
#    Updated: 2026/09/08 11:04:48 by eduaaugu        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def age(self):
        self.days += 1

    def grow(self, growth):
        self.height += growth

    def show(self):
        print(f"{self.name}: {round(self.height, 2)}cm, {self.days} days old")

def ft_plant_factory(plants: dict[str, Plant]):
    print("=== Plant Factory Output ===")
    for plant in plants.values():
        print("Created:", end=" ")
        plant.show()

def main():
    plants = {
            "rose": Plant("Rose", 25.0, 30),
            "oak": Plant("Oak", 200.0, 365),
            "cactus": Plant("Cactus", 5.0, 90),
            "sunflower": Plant("Sunflower", 80.0, 45),
            "fern": Plant("Fern", 15.0, 120)
            }
    ft_plant_factory(plants)

if __name__ == "__main__":
    main()
