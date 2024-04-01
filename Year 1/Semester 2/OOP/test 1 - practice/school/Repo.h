#pragma once
#include <iostream>
#include <vector>
#include "School.h"

using namespace std;

class Repo
{
private:
	//list of schools
	vector<School> schools;

public:
	Repo();



	void addSchool(School s);

	void removeSchool(string name);

	vector<School> getSchools() const;
	vector<School> getSchoolsSortedByName() const;

	vector<School> getSchoolsBeforeDate(string date) const;
	vector<School> getSchoolsAfterDate(string date) const;
};

