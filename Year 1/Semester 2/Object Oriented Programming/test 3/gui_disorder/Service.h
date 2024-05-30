#pragma once
#include<Repository.h>
#include<vector>
using namespace std;

class Service
{
private:
	Repository repository;

public:
	vector<Disorder> getAllDisorders();
	vector<string> getAllSymptomsFromName(string name);
};

