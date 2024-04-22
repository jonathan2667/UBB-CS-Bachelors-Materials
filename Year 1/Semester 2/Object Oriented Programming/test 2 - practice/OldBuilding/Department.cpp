#include "Department.h"
#include<string>

string Building::toString() {
	return "Address : " + address + "\nConstruction Year : " + to_string(constructionYear)  + "\n";
}

string Flats::toString() {
	return "Flat\n" + Building::toString() + "nrApp : " + to_string(nrApp) + "\noccupiedApp : " + to_string(occupiedApp);
}

string House::toString() {
	return "House\n" + Building::toString() + "type :" + type + "\nisHistorical : " + to_string(isHistorical);
}

bool Flats::canBeDemolished() {
	double percentage = double(occupiedApp) / double(nrApp);
	if (percentage <= 0.05) return true;
	return false;
}

bool Flats::mustBeRestored() {
	double percentage = double(occupiedApp) / double(nrApp);
	if (percentage > 0.80 and 2024 - constructionYear >= 40) return true;
	return false;
}

bool House::canBeDemolished() {
	return isHistorical;
}

bool House::mustBeRestored() {
	if (2024 - constructionYear >= 100) return true;
	return false;
}

