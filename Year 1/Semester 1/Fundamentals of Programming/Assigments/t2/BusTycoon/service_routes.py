from repository_routes import RepositoryRoute

class ServiceRoute:
    def __init__(self):
        self.__data = RepositoryRoute()

    def get_all(self):
        return self.__data.get_all_routes_repo()

    def get_km_by_code(self, code):
        all_routes = self.get_all()
        for route in all_routes:
            if route.code == code:
                return route.length

