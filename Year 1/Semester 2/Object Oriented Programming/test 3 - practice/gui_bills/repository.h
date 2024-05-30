#pragma once
#include<vector>
#include<bills.h>
#include<fstream>
#include<sstream>
using namespace std;

class repository
{
private:
	vector<bills> billsList;
public:
	repository() { this->loadRepo(); };
	void loadRepo();
	vector<bills> getBills() const { return this->billsList; };
};

