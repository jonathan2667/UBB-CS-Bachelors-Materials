#pragma once
#include "Repository.h"
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
using namespace std;

class Service
{
private:
	Repository repo;
public:
	vector<Car> getAllCars() const;
	vector<Car> getCarsByManufacturer(string manufacturer) const;
};

