#include "Repo.h"
#include<algorithm>
Repo::Repo() {
	this->schools.push_back(School("Avram Iancu", {46.33, 45.33}, "15.04.2022", false));
	this->schools.push_back(School("Mihai Viteazul", { 46.33, 45.33 }, "16.04.2022", false));
	this->schools.push_back(School("Gheorghe Sincai", { 46.33, 45.33 }, "17.04.2022", false));
	this->schools.push_back(School("Gheorghe Lazar", { 46.33, 45.33 }, "18.04.2022", false));
	this->schools.push_back(School("Gheorghe Asachi", { 46.33, 45.33 }, "19.04.2022", false));
}

vector<School> Repo::getSchools() const {
	return this->schools;
}

vector<School> Repo::getSchoolsSortedByName() const {
	vector<School> schoolsCopy = this->schools;
	sort(schoolsCopy.begin(), schoolsCopy.end(), [](School s1, School s2) {
		return s1.getName() < s2.getName();
	});
	return schoolsCopy;

}

vector<School> Repo::getSchoolsBeforeDate(string date) const {
	vector<School> schoolsCopy = this->getSchools();
	vector<School> result;
	for (School s : schoolsCopy) {
		if (s.isDateBefore(date)) { 
			result.push_back(s);
		}
	}
	return result;
}

vector<School> Repo::getSchoolsAfterDate(string date) const {
		
	vector<School> schoolsCopy = this->getSchools();
	vector<School> result;
	for (School s : schoolsCopy) {
		if (s.isDateAfter(date)) {
			result.push_back(s);
		}
	}
	return result;

}

void Repo::addSchool(School s) {
	this->schools.push_back(s);
}

void Repo::removeSchool(string name) {
	bool found = false;
	vector<School>::iterator it;
	for (it = this->schools.begin(); it != this->schools.end(); it++) {
		if (it->getName() == name) {
			this->schools.erase(it);
			found = true;
			break;
		}
	}
	
	if (!found) {
		throw exception("School not found!");
	}
}