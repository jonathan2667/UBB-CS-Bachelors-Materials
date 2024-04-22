#pragma once
#include "Department.h"
#include<vector>

class Controller
{
private:
	vector<Building*> Buildings;
public:
	Controller() {
		Building *house1 = new House("str asda", 2202, "casa", true);
		Building *house2 = new House("str 2da3a", 2012, "casa", true);

		Building *flat1 = new Flats("str dwa", 2022, 22, 23);
		Building *flat2 = new Flats("str aaaa", 2105, 5, 10);

		Buildings.push_back(flat1);
		Buildings.push_back(flat2);
		Buildings.push_back(house1);
		Buildings.push_back(house2);

	}
	~Controller() {
		for (auto building : Buildings) delete building;
	}
	void addBuilding(Building * a);
	vector<Building*> getAll() { return this->Buildings; }
	bool adressAlready(string addressGiven) {
		for (auto building : Buildings) {
			if (building->address == addressGiven) return true;
		}
		return false;
	}
	void writeToFileRestored(string file);
	void writeToFileDemolished(string file);
};

