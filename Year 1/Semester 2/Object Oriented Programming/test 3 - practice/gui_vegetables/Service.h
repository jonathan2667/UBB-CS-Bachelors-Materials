#pragma once
#include<Repository.h>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

class Service
{
private:
	Repository repository;

public:
	vector<Vegetables> getAllVegetables();
	vector<string> getAllUniqueFamilies();
	vector<Vegetables> getAllVegetablesBelongingToFamily(string family);
	Vegetables getVegetableFromName(string name);
};

