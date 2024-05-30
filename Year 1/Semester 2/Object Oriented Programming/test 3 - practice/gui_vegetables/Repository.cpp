#include "Repository.h"

Repository::Repository() {
	loadFromFile();
}

void Repository::loadFromFile() {
	ifstream file("vegetables.txt");
	string line;
	string family, name, list;
	const char del = '|';
	while (getline(file, line)) {
		istringstream iss(line);
		getline(iss, family, del);
		getline(iss, name, del);
		getline(iss, list, del);
		allVegetables.push_back(Vegetables(family, name, list));
	}
}