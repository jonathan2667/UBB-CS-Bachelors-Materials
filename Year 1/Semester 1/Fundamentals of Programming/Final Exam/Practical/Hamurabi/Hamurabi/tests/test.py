import unittest
from service.cityservice import CityService


class test(unittest.TestCase):
    def setUp(self):
        self.__service = CityService()

    def test_is_lose(self):
        if self.__service.get_city_management().starving_people > self.__service.get_city_management().population // 2:
            self.assertTrue(self.__service.is_lose())
        else:
            self.assertFalse(self.__service.is_win())

    def test_is_win(self):
        if self.__service.get_city_management().acres_of_land < 1000 and self.__service.get_city_management().population < 100:
            self.assertTrue(self.__service.is_win())
        else:
            self.assertFalse(self.__service.is_win())

    def test_set_land_price(self):
        self.__service.set_land_price(27)
        self.assertEqual(27, self.__service.get_city_management().land_price)
        self.__service.set_land_price(15)
        self.assertEqual(15, self.__service.get_city_management().land_price)
        self.__service.set_land_price(10)
        self.assertEqual(10, self.__service.get_city_management().land_price)

    def test_sell_or_buy_acres(self):
        acres = self.__service.get_city_management().acres_of_land
        self.__service.sell_or_buy_acres(0)
        self.assertEqual(acres, self.__service.get_city_management().acres_of_land)

    def test_feed_population(self):
        stocks = self.__service.get_city_management().stocks
        self.__service.feed_population(200)
        self.assertEqual(stocks - 200, self.__service.get_city_management().stocks)