#include "Ui.h"
#include<iostream>

using namespace std;

Ui::Ui() {
	;
}

void Ui::printSchools() {
	vector<School> schools = this->service.getSchools();
	for (School school : schools) {
		cout << school.toString() << endl;
	}
	//print schools sorted by name
	cout << "Sorted by name: " << endl;
	vector<School> sortedByName = this->service.getSchoolsSortedByName();
	for (School school : sortedByName) {
		cout << school.toString() << endl;
	}
}

void Ui::printMenu() {
	cout << "1. Add school" << endl;
	cout << "2. Remove school" << endl;
	cout << "3. Print schools Sorted" << endl;
	cout << "4. Print schools schools having planned date before a given date and after" << endl; // "Print schools having planned date before a given date"
	cout << "5. Exit" << endl;
}

void Ui::addSchool() {
	//this->schools.push_back(School("Avram Iancu", {46.33, 45.33}, "15.04.2022", false));
	string name;
	cout << "Name: ";
	cin >> name;

	cout << "Latitude: ";
	float latitude;
	cin >> latitude;

	cout << "Longitude: ";
	float longitude;
	cin >> longitude;

	string date;
	cout << "Date: ";
	cin >> date;

	int schoolWasVisited;
	cout << "School was visited: 1 for True, 2 for False ";
	cin >> schoolWasVisited;
	if (schoolWasVisited == 1) {
		this->service.addSchool(School(name, { latitude, longitude }, date, true));
	}
	else {
		this->service.addSchool(School(name, { latitude, longitude }, date, false));
	}
	
}

void Ui::removeSchool() {
	string name;
	cout << "Name: ";
	cin.get();
	getline(cin, name);
	try {
		this->service.removeSchool(name);
	}
	catch (exception& e) {
		cout << e.what() << endl;
	}
}

void Ui::printSchoolsBeforeAndAfterGivenDate() {
	string date;
	cout << "Date: ";
	cin >> date;

	cout << "Schools before date: " << endl;
	vector<School> schoolsBeforeDate = this->service.getSchoolsBeforeDate(date);
	for (School school : schoolsBeforeDate) {
		cout << school.toString() << endl;
	}

	cout << "Schools after date: " << endl;
	vector<School> schoolsAfterDate = this->service.getSchoolsAfterDate(date);
	for (School school : schoolsAfterDate) {
		cout << school.toString() << endl;
	}

}
void Ui::run() {
		while (true) {
		this->printMenu();
		int command;
		cin >> command;
		if (command == 1) {
			this->addSchool();
		}
		else if (command == 2) {
		    this->removeSchool();
		}
		else if (command == 3) {
			this->printSchools();
		}
		else if (command == 4) {
			this->printSchoolsBeforeAndAfterGivenDate();
		}
		else if (command == 5) {
			break;
		}
	}

}



int main() {
	Ui ui = Ui();
	ui.run();
}