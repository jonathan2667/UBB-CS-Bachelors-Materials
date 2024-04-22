#include "UI.h"
#include<iostream>

using namespace std;

void UI::run() {
	int option;
	while (1) {
		cout << "1) Add a new department\n2) Show all departments\n3) Show all efficient departments\n4) Write all the departments to a file\n5) Exit the applciation\nSelect you option: ";
		cin >> option;
		if (option == 1) this->addDepartment();
		if (option == 2) this->showAllDepartments();
		if (option == 3) this->showAllEfficientDepartments();
		if (option == 4) this->writeToFile();
	}
}

void UI::addDepartment() {
	int option;
	cout << "1. NeoNatal \n2. SurgeryUnit \n";
	cin >> option;

	string hospitalName;
	int numberOfDoctors;

	cout << "Enter the name of the hospital: \n";
	cin >> hospitalName;
	cout << "Enter the number of doctors: \n";
	cin >> numberOfDoctors;

	
	if (option == 1) {
		double averageGrade;
		int numberOfMothers, numberOfNewborns;
		cout << "Enter the averageGrade: \n";
		cin >> averageGrade;
		cout << "Enter the numberOfMothers: \n";
		cin >> numberOfMothers;
		cout << "Enter the numberOfNewborns: \n";
		cin >> numberOfNewborns;

		this->appController.addDepartment(new NeonantalUnit(hospitalName, numberOfDoctors, averageGrade
			, numberOfMothers, numberOfNewborns));
	}
	else if (option == 2) {
		int numberOfPacients;
		cout << "Enter the numberOfPacients: \n";
		cin >> numberOfPacients;
		this->appController.addDepartment(new Surgery(hospitalName, numberOfDoctors, numberOfPacients));
	}
	else {
		cout << "INVALID"; 
		return;
	}
}

void UI::showAllDepartments() {
	vector<HospitalDepartment*> departments = this->appController.getAllDepartments();
	for (auto department : departments)
		cout << department->toString() << "\n";
}

void UI::showAllEfficientDepartments() {
	vector<HospitalDepartment*> departments = this->appController.getAllEficientDepartments();
	for (auto department : departments)
		cout << department->toString() << '\n';
}

void UI::writeToFile() {
	string filename;
	cout << "FileName\n";
	cin >> filename;
	this->appController.writeToFile(filename);
}