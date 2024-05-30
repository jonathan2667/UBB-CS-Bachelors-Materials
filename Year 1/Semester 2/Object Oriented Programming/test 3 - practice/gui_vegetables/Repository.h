#pragma once
#include<vector>
#include<sstream>
#include<fstream>
#include<Vegetables.h>
using namespace std;

class Repository
{
private:
	vector<Vegetables> allVegetables;
public:
	Repository();
	void loadFromFile();
	vector <Vegetables> getAllVegetables() { return allVegetables; }
};

