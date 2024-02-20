from repository_bus import RepositoryBus

class BusService:

    def __init__(self):
        self.__data = RepositoryBus()

    def get_all(self):
        return self.__data.get_all_bus_repo()

    def get_code_and_time_used_by_id(self, id):
        all_buses = self.get_all()
        for bus in all_buses:
            if bus.id == id:
                return (bus.route_code, bus.time_used_on_route)