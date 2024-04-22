#include "UI.h"
#include "Applicance.h"

void UI::run() {
	cout << "Welcome to the Appliance Store!\n";
	int option;
	while (1) {
		cout << "1.Add appliance.\n2.Show all";
		cout << "\n3.Show all inefficient\n4.Save to file\n5.Exit\n";
		cin >> option;
		if (option == 1) this->addAppliance();
		else if (option == 2) this->showAppliances();
		else if (option == 3) this->showInefficient();
		else if (option == 4) this->saveToFile();
		else break;
	}
}

void UI::saveToFile() {
	string fileName;
	cout << "FileName:\n";
	cin >> fileName;
	int value;
	cout << "Value:\n";
	cin >> value;
	appController.writeToFile(fileName, value);
}

void UI::showInefficient() {
	vector< Appliance*> Appliances = appController.getInefficientAppliances();
	for (auto appliance : Appliances)
		cout << appliance->toString() << '\n';
}
void UI::showAppliances() {
	vector< Appliance*> Appliances = appController.getAppliances();
	for (auto appliance : Appliances)
		cout << appliance->toString() << '\n';
}

void UI::addAppliance() {
	int option;
	cout << "Press 1 for Refrigerator and 2 for Dish Washing\n";
	cin >> option;

	string id;
	cout << "Id:\n";
	cin >> id;

	if (option == 1) {
		string electricityUsageClass;
		bool hasFreezer;

		cout << "electricityUsageClass: either A, A+, A++ (default is A)\n";
		cin >> electricityUsageClass;
		if (electricityUsageClass != "A" or electricityUsageClass != "A+" or
			electricityUsageClass != "A++") electricityUsageClass = "A";

		string prevOption;
		cout << "hasFreezer, 1 or 0: (default is 0)";
		cin >> prevOption;
		if (prevOption != "0" and prevOption != "1") hasFreezer = 0;
		else {
			if (prevOption == "1") hasFreezer = 1;
			else if (prevOption == "0") hasFreezer = 0;
			else hasFreezer = 0;
		}

		appController.addAppliance(new Refrigerator(id, electricityUsageClass, hasFreezer));
	}
	else if (option == 2) {
		double consumedElectricityForOneHour;
		cout << "consumedElectricityForOneHour: (default is 0)\n";
		cin >> consumedElectricityForOneHour;

		appController.addAppliance(new DishWasher(id, consumedElectricityForOneHour));
	}
	else {
		cout << "Invalid";
		return;
	}

}

int main() {
	UI ui;
	ui.run();
	return 0;
}