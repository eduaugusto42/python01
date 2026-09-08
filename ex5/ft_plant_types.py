# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/08 15:11:04 by eduaaugu         #+#    #+#              #
#    Updated: 2026/09/08 16:47:56 by eduaaugu        ###   ########.fr        #
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

class Flower(Plant):
    def bloom(self):

class Tree(Plant):
    def produce_shade(self):

class Vegetable(Plant):
    def nutritional_value(self):

def main():

if __name__ == "__main__":
    main()
