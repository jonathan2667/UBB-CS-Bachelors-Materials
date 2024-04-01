#pragma once

#include "Repo.h"
#include "School.h"
#include <vector>

class Service
{
private:
	Repo repo = Repo();
public:
	Service();
	
	vector<School> getSchools() const;
	vector<School> getSchoolsSortedByName() const;
	vector<School> getSchoolsBeforeDate(string date) const;
	vector<School> getSchoolsAfterDate(string date) const;
	void addSchool(School s);
	void removeSchool(string name);
};

