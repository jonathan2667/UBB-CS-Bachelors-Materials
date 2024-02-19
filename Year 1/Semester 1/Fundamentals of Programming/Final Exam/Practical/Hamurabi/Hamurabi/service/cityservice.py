import random

from domain.CityManagement import CityManagement


class CityService:
    def __init__(self):
        self.__city_management = CityManagement()

    def get_city_management(self):
        """
        we get the board for printing
        :return: city management(all information about the game!)
        """
        return self.__city_management

    def is_lose(self):
        """
        we check if the game is over
        if more than half of people died is game over
        :return: True if game over False otherwise
        """
        if self.__city_management.starving_people >= self.__city_management.population / 2:
            return True
        return False

    def is_win(self):
        """
        We check if the game is won
        if we have more then 100 people and more as 1000 acres of land we won
        :return: true if win false otherwise
        """
        if self.__city_management.population > 100 and self.__city_management.acres_of_land > 1000:
            return True
        return False

    def set_land_price(self, number):
        """
        here we set the land price
        :param number:
        :return:
        """
        self.__city_management.set_land_price(number)

    def set_harvest_units(self, number):
        """
        here we set the harvest units
        :param number:
        :return:
        """
        self.__city_management.set_harvest(number)

    def test_acres_to_sell_or_buy(self, number):
        """
        testing input data
        :param number:
        :return:
        """
        if number <= 0:
            if self.__city_management.acres_of_land + number < 0:
                return False
        elif self.__city_management.stocks < number * self.__city_management.land_price:
                return False

        return True

    def sell_or_buy_acres(self, number: int):
        """
        here we will sell or buy acres
        if the number is negative we sell
        else we buy
        we update the stocks accordingly
        :param number:
        :return:
        """
        if number <= 0:
            self.__city_management.set_acres(number)
            self.__city_management.set_stocks(-number * self.__city_management.land_price + self.__city_management.stocks)
        else:
            self.__city_management.set_acres(number)
            self.__city_management.set_stocks(self.__city_management.stocks - number * self.__city_management.land_price)

    def test_units_to_feed(self, number: int, acres_to_sell_or_buy):
        if number > self.__city_management.stocks - acres_to_sell_or_buy * self.__city_management.land_price:
            return False
        return True

    def feed_population(self, number: int):
        """
        we feed the population
        we subtract from the stocks the amount feed
        :param number:
        :return:
        """
        self.__city_management.feed_population(number)

    def test_acres_to_plant(self, number: int, units_to_feed, add_stock):
        """
        test input data
        here we test if we have enough grain to plant
        :param number:
        :param units_to_feed:
        :param add_stock:
        :return:
        """
        if self.__city_management.acres_of_land < number:
            return False

        if self.__city_management.stocks - units_to_feed - self.__city_management.land_price * add_stock < number:
            return False

        return True

    def plant_acres(self, number: int):
        """

        :param number: how many acres we plant
        we will set the acres planted to number
        :return:
        """
        number = min(number, self.__city_management.population * 10)
        self.__city_management.plant_acres(number)

    def rat_infest(self):
        """
        we have a 20 percent change to pick a number between 1 and 2 in range(1, 10)
        if we pick 1 or 2 we have a rat infestation
        the maximum number of grains ate by the rats are stocks/100*20(20%)
        :return:
        """
        number = random.randint(1, 10)

        if number <= 2:
            units = random.randint(0, int(self.__city_management.stocks / 100 * 20))
            self.__city_management.set_rat_units(units)
            self.__city_management.set_stocks(self.__city_management.stocks - units)
        else:
            self.__city_management.set_rat_units(0)