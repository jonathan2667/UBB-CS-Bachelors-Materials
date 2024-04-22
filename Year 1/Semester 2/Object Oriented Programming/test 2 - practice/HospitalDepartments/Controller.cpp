#include "Controller.h"
#include<fstream>
void Controller::addDepartment(HospitalDepartment* department) {
	this->departments.push_back(department);
}

vector<HospitalDepartment*> Controller::getAllDepartments() {
	return this->departments;
}

vector<HospitalDepartment*> Controller::getAllEficientDepartments() {
	vector<HospitalDepartment*> efficientDepartments;
	for (auto department : this->departments)
		if (department->isEficient())
			efficientDepartments.push_back(department);
	return efficientDepartments;
}

void Controller::writeToFile(std::string fileName)
{
	//std::sort(this->departments.begin(), this->departments.end(), comparisonFunction);
	ofstream fin(fileName);
	for (auto department : this->departments)
		fin << department->toString() << '\n';
}


