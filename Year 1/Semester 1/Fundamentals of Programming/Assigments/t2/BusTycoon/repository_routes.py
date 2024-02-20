from domain_routes import Route

class RepositoryRoute:
    def __init__(self):
        self.__all_routes = []
        self.get_routes_from_text_repo()

    def add_routes_repo(self, route):
        self.__all_routes.append(route)

    def get_all_routes_repo(self):
        return self.__all_routes


    def get_routes_from_text_repo(self):
        with open('buses_routes.txt', 'r') as file:
            rows = file.readlines()

        for row in rows:
            code, kms = [item.strip() for item in row.split(',')]
            new = Route(int(code), int(kms))
            self.add_routes_repo(new)