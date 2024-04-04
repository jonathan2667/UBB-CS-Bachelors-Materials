#pragma once
#include "Service.h"

class Ui
{
private:
	Service service = Service();

public:
	Ui();

	void printSchools();
	void addSchool();
	void removeSchool();
	void printMenu();
	void printSchoolsBeforeAndAfterGivenDate();
	void run();
};

