#include "Service.h"
#include<algorithm>
vector<Car> Service::getAllCars() const
{
	vector<Car> cars = repo.getAllCars();
	sort(cars.begin(), cars.end());
	return cars;
}

vector<Car> Service::getCarsByManufacturer(string manufacturer) const
{
	vector<Car> allCars = repo.getAllCars();
	vector<Car> cars;
	for (const Car& c : allCars)
		if (c.getManufacturer() == manufacturer)
			cars.push_back(c);
	return cars;
}