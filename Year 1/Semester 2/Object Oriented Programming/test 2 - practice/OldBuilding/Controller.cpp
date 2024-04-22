#include "Controller.h"
#include<fstream>

void Controller::addBuilding(Building * a) {
	Buildings.push_back(a);
}

void Controller::writeToFileRestored(string file) {
	ofstream fout(file);
	for (auto building : Buildings)
		if (building->mustBeRestored()) fout << building->toString() << '\n';
}

void Controller::writeToFileDemolished(string file) {
	ofstream fout(file);
	for (auto building : Buildings)
		if (building->canBeDemolished()) fout << building->toString() << '\n';
}