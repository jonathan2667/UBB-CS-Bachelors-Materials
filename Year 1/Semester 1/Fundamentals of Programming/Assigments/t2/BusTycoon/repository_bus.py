from domain_bus import Bus

class RepositoryBus:
    def __init__(self):
        self.__all_buses = []
        self.get_all_bus_from_text_repo()

    def add_bus_repo(self, bus):
        self.__all_buses.append(bus)

    def get_all_bus_repo(self):
        return self.__all_buses

    def get_all_bus_from_text_repo(self):
        with open('buses.txt', 'r') as file:
            rows = file.readlines()

        for row in rows:
            id, route_code, model, time_used_on_route = [item.strip() for item in row.split(',')]
            new_bus = Bus(int(id), int(route_code), model, int(time_used_on_route))
            self.add_bus_repo(new_bus)

    def update_all_bus_to_text_repo(self):
        with open('buses.txt', 'w') as file:
            for bus in self.get_all_bus():
                id = bus.id
                route_code = bus.route_code
                model = bus.model
                time_used_on_route = bus.time_used_on_route
                file.write(str(id) + ', ' + str(route_code) + ', ' + model + ', ' + str(time_used_on_route))

