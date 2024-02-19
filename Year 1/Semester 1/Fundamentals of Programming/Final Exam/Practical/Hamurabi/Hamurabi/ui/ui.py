
from service.cityservice import CityService
import random


class Ui:
    def __init__(self):
        self.__service = CityService()

    def test_input(self, acres_to_sell_or_buy, units_to_feed, acres_to_plant):
        if not self.__service.test_acres_to_sell_or_buy(acres_to_sell_or_buy):
            raise ValueError("Not enough money!")

        add_stock = acres_to_sell_or_buy

        if not self.__service.test_units_to_feed(units_to_feed, add_stock):
            raise ValueError("Not enough food!")


        if not self.__service.test_acres_to_plant(acres_to_plant, units_to_feed, add_stock):
            raise ValueError("Invalid input for acres!")

    def decide(self):
        """
        Here we have the ui for deciding the next year
        we will perform the operations as stated in the task
        :return:
        """
        acres_to_sell_or_buy = int(input("Acres to buy/sell(+/-)-> "))
        units_to_feed = int(input("Units to feed the population -> "))
        acres_to_plant = int(input("Acres to plant -> "))
        try:
            self.test_input(acres_to_sell_or_buy, units_to_feed, acres_to_plant)

            land_price = random.randint(15, 25)
            harvest_units = random.randint(1, 6)

            self.__service.sell_or_buy_acres(acres_to_sell_or_buy)
            self.__service.feed_population(units_to_feed)
            self.__service.set_harvest_units(harvest_units)
            self.__service.plant_acres(acres_to_plant)
            self.__service.set_land_price(land_price)
            self.__service.rat_infest()
        except ValueError as ve:
            raise ValueError(ve)

    def run_ui(self):
        win = 0
        cnt = 0

        while True:
            if cnt == 5:
                break
            try:
                print(self.__service.get_city_management())

                self.decide()

                if self.__service.is_win():
                    print(self.__service.get_city_management())
                    print("Congratulations! YOU WON!!!")
                    win = 1
                    break

                if self.__service.is_lose():
                    win = 0
                    print(self.__service.get_city_management())
                    break

                cnt += 1

            except ValueError as ve:
                print(ve)

        if not win:
            print("LOSE!")
