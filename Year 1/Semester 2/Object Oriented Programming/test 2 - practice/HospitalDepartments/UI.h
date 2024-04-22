#pragma once
#include "Controller.h"
class UI
{
private:
	Controller appController;
public:
	UI() {};
	~UI() {};

	void run();
	void addDepartment();
	void showAllDepartments();
	void showAllEfficientDepartments();
	void writeToFile();
};

