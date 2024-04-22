#pragma once
#include <string>

using namespace std;

class Departments
{
};

class HospitalDepartment {
protected:
	string hospitalName;
	int numberOfDoctors;

public:
	HospitalDepartment() : hospitalName{ "" }, numberOfDoctors{0} {};
	HospitalDepartment(string hospitalName, int numberOfDoctors) : hospitalName{ hospitalName }, numberOfDoctors{ numberOfDoctors } {};
	virtual bool isEficient() { return false; }
	virtual string toString();
	string getName() { return this->hospitalName; }
};

class NeonantalUnit : public HospitalDepartment {
public:
	double averageGrade;
	int numberOfMothers, numberOfNewborns;
	NeonantalUnit(string hospitalName, int numberOfDoctors, double averageGrade, int numberOfMothers, int numberOfNewborns) :
		HospitalDepartment{ hospitalName, numberOfDoctors }, averageGrade{ averageGrade }, numberOfMothers{ numberOfMothers },
			numberOfNewborns{ numberOfNewborns } {};
	bool isEficient();
	string toString();
};

class Surgery : public HospitalDepartment {
private:
	int numberOfPacients;
public: 
	Surgery(string hospitalName, int numberOfDoctors, int numberOfPacients) :
		HospitalDepartment{ hospitalName, numberOfDoctors }, numberOfPacients{ numberOfPacients } {};
	bool isEficient();
	string toString();
};
