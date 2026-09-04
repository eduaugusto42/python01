# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: eduaaugu <eduaaugu@student.42sp.org.br>   +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/03 17:06:25 by eduaaugu         #+#    #+#              #
#    Updated: 2026/09/04 17:05:52 by eduaaugu        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")

def main():
    cactus = Plant("Cactus", 15, 120)
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)

    print("== Garden Plant Registry ==")
    rose.show()
    sunflower.show()
    cactus.show()

if __name__ == "__main__":
    main()
