#pragma once
#include<string>
using namespace std;

class Appliance {
public:
	string id;


	Appliance(string id) : id{ id } {};
	virtual string toString();
	virtual double consumedElectricity() { return 0; };
};

class Refrigerator : public Appliance {
public:
	string electricityUsageClass;
	bool hasFreezer;


	Refrigerator(string id, string electricityUsageClass, bool hasFreezer) :
		Appliance{ id }, electricityUsageClass{ electricityUsageClass }, hasFreezer{ hasFreezer } {};
	string toString();
	double consumedElectricity();
};

class DishWasher : public Appliance {
public:
	double consumedElectricityForOneHour;


	DishWasher(string id, double consumedElectricityForOneHour) :
		Appliance{ id }, consumedElectricityForOneHour{ consumedElectricityForOneHour } {};
	string toString();
	double consumedElectricity();
};