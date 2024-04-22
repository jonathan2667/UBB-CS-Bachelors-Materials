#pragma once
#include<vector>
#include "Departments.h"

class Controller
{
private :
	vector<HospitalDepartment *> departments;
public:
	Controller() {
		HospitalDepartment *neonantal1 = new NeonantalUnit("1", 11, 12, 13, 14);
		HospitalDepartment* neonantal2 = new NeonantalUnit("2", 21, 22, 23, 24);

		HospitalDepartment* surgery1 = new Surgery("1", 31, 32);
		HospitalDepartment* surgery2 = new Surgery("2", 41, 42);

		departments.push_back(neonantal1);
		departments.push_back(neonantal2);
		departments.push_back(surgery1);
		departments.push_back(surgery2);
	}
	~Controller() {
		for (auto department : departments) {
			delete department;
		}
	}
	void addDepartment(HospitalDepartment* department);
	vector<HospitalDepartment*> getAllDepartments();
	vector<HospitalDepartment*> getAllEficientDepartments();
	void writeToFile(string fileName);
};

