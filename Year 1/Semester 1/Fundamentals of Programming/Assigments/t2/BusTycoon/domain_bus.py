from dataclasses import dataclass

@dataclass
class Bus:
    __id: int
    __route_code: int
    __model: str
    __time_used_on_route: int

    @property
    def id(self):
        return self.__id

    @property
    def route_code(self):
        return self.__route_code

    @property
    def model(self):
        return self.__model

    @property
    def time_used_on_route(self):
        return self.__time_used_on_route