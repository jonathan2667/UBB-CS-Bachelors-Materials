#pragma once
#include<iostream>
#include "Controller.h"
using namespace std;

class UI
{
public:
	Controller appController;

	void run();
	void addAppliance();
	void showAppliances();
	void showInefficient();
	void saveToFile();
};

