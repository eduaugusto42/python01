def main():
    cactus = Plant("Cactus", 15, 120)
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)

    print("== Garden Plant Registry ==")
    rose.show()
    sunflower.show()
    cactus.show()

class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")

if __name__ == "__main__":
    main()
