from dataclasses import dataclass

@dataclass
class Entity():
    __id: int
    __name: str

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return str(self.__id) + " " + self.__name