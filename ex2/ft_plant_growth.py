# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_growth.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/03 17:58:12 by eduaaugu         #+#    #+#              #
#    Updated: 2026/09/04 17:33:25 by eduaaugu        ###   ########.fr        #
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

def ft_plant_growth(plant: Plant, growth: float | int):
    initial_height = plant.height

    print("=== Garden Plant Growth ===")
    plant.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.age()
        plant.grow(growth)
        plant.show()
    print(f"Growth this week: {round(plant.height - initial_height, 2)}cm")

def main():
    rose = Plant("Rose", 25.0, 30)
    ft_plant_growth(rose, 0.8)

if __name__ == "__main__":
    main()
