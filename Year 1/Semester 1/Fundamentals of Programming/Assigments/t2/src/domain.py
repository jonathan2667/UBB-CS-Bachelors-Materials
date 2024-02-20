from dataclasses import dataclass

@dataclass

class Player:
    __id: int
    __name: str
    __strength: int

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        self.__strength = value

    def __str__(self):
        return "Id: " + str(self.__id) + " Name: " + str(self.__name) + " Strength: " +  str(self.__strength)
