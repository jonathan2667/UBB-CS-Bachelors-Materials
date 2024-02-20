from dataclasses import dataclass

@dataclass
class Route:
    __code: int
    __length: int

    @property
    def code(self):
        return self.__code

    @property
    def length(self):
        return self.__length
