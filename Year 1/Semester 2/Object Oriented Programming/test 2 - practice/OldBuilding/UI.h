#pragma once
#include "Controller.h"
#include<iostream>
using namespace std;

class UI
{
private:
	Controller appController;
public:
	void run();
	void addBuilding();
	void showAllBuildings();
	void showAllBuildingsSorted();
	void saveFile();
};

