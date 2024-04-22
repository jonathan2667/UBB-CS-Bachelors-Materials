#pragma once
#include "Applicance.h"
#include<vector>
using namespace std;

class Controller
{
private:
	vector< Appliance*> Appliances;
public:
	Controller();
	~Controller();
	void addAppliance(Appliance* a);
	vector< Appliance*> getAppliances();
	vector< Appliance*> getInefficientAppliances();
	vector< Appliance*> sortAppliancesValue(int value);
	void writeToFile(string fileName, int value);
};

