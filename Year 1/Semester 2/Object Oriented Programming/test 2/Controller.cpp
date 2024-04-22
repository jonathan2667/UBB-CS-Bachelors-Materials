#include "Controller.h"
#include<fstream>
#include<algorithm>

Controller::Controller() {
	Appliance* refrigerator1 = new Refrigerator("1a", "A", true);
	Appliance* refrigerator2 = new Refrigerator("1b", "A+", true);
	Appliance* refrigerator3 = new Refrigerator("1aa", "A+", true);

	Appliance* dishwasher1 = new DishWasher("2a", 20);
	Appliance* dishwasher2 = new DishWasher("2b", 50);

	Appliances.push_back(refrigerator1);
	Appliances.push_back(refrigerator2);
	Appliances.push_back(dishwasher1);
	Appliances.push_back(dishwasher2);
	Appliances.push_back(refrigerator3);
}

Controller::~Controller(){
	for (auto appliance : Appliances) delete appliance;
}

void Controller::addAppliance(Appliance* a){
	this->Appliances.push_back(a);
}

vector< Appliance*> Controller::getAppliances() {
	return this->Appliances;
}
vector< Appliance*> Controller::getInefficientAppliances() {
	vector< Appliance*> InefficientAppliances;
	for (auto appliance : Appliances)
		if (appliance->consumedElectricity() > 100)
			InefficientAppliances.push_back(appliance);
	return InefficientAppliances;
}

vector< Appliance*> Controller::sortAppliancesValue(int value) {
	vector< Appliance*> SortedAppliances;
	for (auto appliance : Appliances)
		if (appliance->consumedElectricity() < value)
			SortedAppliances.push_back(appliance);
	sort(SortedAppliances.begin(), SortedAppliances.end(), [](Ap
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		


















		
+
		




		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		/2q+
		e* a, Appliance* b)
		{return a->id < b->id; });
	return SortedAppliances;
}

void Controller::writeToFile(string fileName, int value) {
	ofstream fout(fileName);
	vector< Appliance*> SortedAppliancesSmallerThanValue = sortAppliancesValue(value);
	for (auto appliance : SortedAppliancesSmallerThanValue)
		fout << appliance->toString() << '\n';
}