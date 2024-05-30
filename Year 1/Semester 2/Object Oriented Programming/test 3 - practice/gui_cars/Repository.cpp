#include "Repository.h"
#include <fstream>

void Repository::loadFromFile() {
	ifstream file("cars.txt");
	string line;
	while (getline(file, line)) {
		istringstream iss(line);
		string manufacturer, model, colour, yearString;
		int year;
		const char delimiter = '|';
		getline(iss, manufacturer, delimiter);
		getline(iss, model, delimiter);
		getline(iss, yearString, delimiter);
		year = stoi(yearString);
		getline(iss, colour, delimiter);
		cars.push_back(Car(manufacturer, model, colour, year));
	}
	file.close();
}