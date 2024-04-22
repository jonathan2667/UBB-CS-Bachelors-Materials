#include "Departments.h"
#include<string>

string HospitalDepartment::toString()
{
	std::string stringHospital = "Name: " + hospitalName + "\nNumber Of Doctors: " + to_string(numberOfDoctors) + "\n";
	return stringHospital;
}

string NeonantalUnit::toString()
{
	return "Type: Neonatal Unit\n" + HospitalDepartment::toString() + "Average Grade: " + to_string(averageGrade) + " numberOfMothers " + 
		to_string(numberOfMothers) + " numberOfNewborns " + to_string(numberOfNewborns) + '\n';
}

string Surgery::toString()
{
	return "Type: Surgery Unit\n" + HospitalDepartment::toString() + "Number of Pacients: " + std::to_string(numberOfPacients) + '\n';
}

bool NeonantalUnit::isEficient() {
	return averageGrade > 8.5 && numberOfNewborns >= numberOfMothers;
}

bool Surgery::isEficient() {
	double ratio = (double)numberOfPacients / (double)numberOfDoctors;
	return ratio >= 2;
}