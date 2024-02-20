from service_bus import BusService
from service_routes import ServiceRoute
class UI:

    def __init__(self):
        self.__bus_service = BusService()
        self.__route_service = ServiceRoute()
    def run(self):

        while True:
            client_input = input("\n\n1. Print all buses\n2. Print buses according to route\n3.Number kms during"
                                 " service\n4.Display descending by mileage\n")

            if client_input == "1":
                all_buses = self.__bus_service.get_all()
                for bus in all_buses:
                    print(bus)
            elif client_input == "2":
                try:
                    route = int(input("what route?"))
                    all_buses = self.__bus_service.get_all()
                    for bus in all_buses:
                        if bus.route_code == route:
                            print(bus)
                except Exception as ex:
                    print(str(ex))
            elif client_input == "3":
                try:
                    id = int(input("id"))
                    (route_code, time_used) = self.__bus_service.get_code_and_time_used_by_id(id)
                    route_kilimoters = self.__route_service.get_km_by_code(route_code)
                    print("totall kms "+ str(route_kilimoters * time_used))

                except Exception as ex:
                    print(str(ex))
            elif client_input == "4":
                all_buses = self.__bus_service.get_all()
                all_routes = self.__route_service.get_all()
                hashmap = {}
                for bus in all_buses:
                    id = bus.id

                    (route, time_used) = self.__bus_service.get_code_and_time_used_by_id(id)
                    route_kilimoters = self.__route_service.get_km_by_code(route)
                    if route in hashmap:
                        hashmap[route] += route_kilimoters * time_used
                    else:
                        hashmap[route] = route_kilimoters * time_used

                for route in all_routes:
                    found = False
                    for key, value in hashmap.items():
                        if key == route.code:
                            found = True
                    if found == False:
                        hashmap[route.code] = 0


                for key, value in hashmap.items():
                    print(str(key) + "  kms: " + str(value))
                    for bus in all_buses:
                        if bus.route_code == key:
                            print(bus, end = " --- ")
                    print("")
            else:
                print("Invalid Option")