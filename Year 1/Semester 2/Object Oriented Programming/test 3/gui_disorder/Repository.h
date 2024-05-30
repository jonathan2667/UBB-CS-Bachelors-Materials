#pragma once
#include<Disorder.h>
#include<vector>

class Repository
{
private:
	vector<Disorder> disorders;
public:
	Repository() { loadFromFile(); };
	vector<Disorder> getDisorders() { return disorders; };
	void loadFromFile();
};

