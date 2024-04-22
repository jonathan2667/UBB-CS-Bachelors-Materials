#include "UI.h"
#include "Department.h"
#include<string>
#include<algorithm>
void UI::run() {
	int option;
	while (1) {
		cout << "1.Add\n2.Show\n3.Show sorted\n4.Save to file\n5.Exit\n";
		cin >> option;
		if (option == 1) this->addBuilding();
		if (option == 2) this->showAllBuildings();
		if (option == 3) this->showAllBuildingsSorted();
		if (option == 4) this->saveFile();

	}
}

void UI::saveFile() {
	string file1, file2;
	cout << "1. File for restored";
	cin >> file1;
	cout << "2. File for demolished";
	cin >> file2;
	appController.writeToFileRestored(file1);
	appController.writeToFileDemolished(file2);
}

void UI::showAllBuildingsSorted() {
	vector<Building*> Buildings = appController.getAll();
	sort(Buildings.begin(), Buildings.end(), [](Building* a, Building* b) {
		return a->constructionYear < b->constructionYear;
		});
	for (auto building : Buildings)
		cout << building->toString() << '\n';
}

void UI::showAllBuildings() {
	vector<Building*> Buildings = appController.getAll();
	for (auto building : Buildings)
		cout << building->toString() << '\n';
}

void UI::addBuilding() {
	int option;
	cout << "1. Add flat \n2. Add house\n";
	cin >> option;

	string address;
	int constructionYear;
	cout << "Address: \n";
	cin.get();
	getline(cin, address);
	if (appController.adressAlready(address)) {
		cout << "Adress Already Here!\n"; 
	}
	else {
		cout << "ConstructionYear: \n";
		cin >> constructionYear;
		if (option == 1) {
			int nrApp;
			int occupiedApp;
			cout << "NrApp: \n";
			cin >> nrApp;
			cout << "occupiedApp: \n";
			cin >> occupiedApp;
			appController.addBuilding(new Flats(address, constructionYear, nrApp, occupiedApp));
		}
		else if (option == 2) {
			string type;
			bool isHistorical;
			cout << "type: \n";
			cin >> type;
			cout << "isHistorical:\n";
			cin >> isHistorical;
			appController.addBuilding(new House(address, constructionYear, type, isHistorical));
		}
		else {
			return;
		}
	}
}
int main() {
	UI ui;
	ui.run();
	return 0;
}