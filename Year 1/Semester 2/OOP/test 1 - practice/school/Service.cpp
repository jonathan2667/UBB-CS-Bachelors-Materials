#include "Service.h"

Service::Service() {
	;
}

vector<School> Service::getSchools() const{
	return this->repo.getSchools();
}

void Service::addSchool(School s) {
	this->repo.addSchool(s);
}

void Service::removeSchool(string name) {
	this->repo.removeSchool(name);
}

vector<School> Service::getSchoolsSortedByName() const {
	return this->repo.getSchoolsSortedByName();
}

vector<School> Service::getSchoolsBeforeDate(string date) const {
	return this->repo.getSchoolsBeforeDate(date);
}

vector<School> Service::getSchoolsAfterDate(string date) const {
	return this->repo.getSchoolsAfterDate(date);
}