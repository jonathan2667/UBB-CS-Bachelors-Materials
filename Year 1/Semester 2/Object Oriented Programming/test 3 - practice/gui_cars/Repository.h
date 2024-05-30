#pragma once
#include<Car.h>
#include<iostream>
#include<vector>
#include<sstream>

using namespace std;

class Repository
{
private:
	vector<Car> cars;
public:
	void loadFromFile();
	Repository() { loadFromFile(); }
	vector<Car> getAllCars() const { return cars; }

};

