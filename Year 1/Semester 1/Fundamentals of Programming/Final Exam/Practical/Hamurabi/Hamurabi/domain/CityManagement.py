import random


class CityManagement:
    def __init__(self):
        self.__year = 0
        self.__starving_people = 0
        self.__new_people = 0
        self.__population = 0
        self.__acres_of_land = 0
        self.__harvest = 0
        self.__rat_units = 0
        self.__land_price = 0
        self.__stocks = 0
        self.__read_input()

    def set_data(self, year, starving_people, new_people, population, acres_of_land, harvest, rat_units, land_price, stocks):
        self.__year = year
        self.__starving_people = starving_people
        self.__new_people = new_people
        self.__population = population
        self.__acres_of_land = acres_of_land
        self.__harvest = harvest
        self.__rat_units = rat_units
        self.__land_price = land_price
        self.__stocks = stocks

    def set_acres(self, number):
        self.__acres_of_land += number

    def set_land_price(self, number):
        self.__land_price = number

    def set_harvest(self, number):
        self.__harvest = number

    def feed_population(self, number):
        self.__stocks -= number

        feed_population = number // 20

        if feed_population < self.__population:
            self.__starving_people = self.__population - feed_population
            self.__population -= self.__starving_people
        else:
            self.__new_people = random.randint(1, 10)
            self.__population += self.__new_people
            self.__starving_people = 0

    def plant_acres(self, acres):
        self.__stocks = self.__stocks + acres * self.__harvest
        self.__stocks -= acres

    def set_stocks(self, number):
        self.__stocks = number

    def set_rat_units(self, number):
        self.__rat_units = number

    @property
    def stocks(self):
        return self.__stocks

    @property
    def year(self):
        return self.__year

    @property
    def starving_people(self):
        return self.__starving_people

    @property
    def new_people(self):
        return self.__new_people

    @property
    def population(self):
        return self.__population

    @property
    def rat_units(self):
        return self.__rat_units

    @property
    def harvest(self):
        return self.__harvest

    @property
    def acres_of_land(self):
        return self.__acres_of_land

    @property
    def land_price(self):
        return self.__land_price

    def __str__(self):
        return (f"\nIn year {self.__year}, {self.starving_people} people starved\n"
                f"{self.__new_people} people came to the city.\n"
                f"City population is {self.__population} people.\n"
                f"Harvest was {self.__harvest} units per acre.\n"
                f"City own {self.__acres_of_land} acres of land.\n"
                f"Rats ate {self.__rat_units} units per acre.\n"
                f"Land price is {self.__land_price} units per acre.\n"
                f"\nGrain stocks are {self.__stocks}\n")

    @staticmethod
    def is_int(number):
        if number[-1] == "," or number[-1] == ".":
            number = number[:len(number) - 1]

        try:
            number = int(number)
            return number
        except ValueError:
            return -1

    def __read_input(self):
        data = []

        with open("year1.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue

                line = line.split(" ")

                for word in line:
                    if self.is_int(word) >= 0:
                        data.append(self.is_int(word))

        self.set_data(*data)
