#pragma once
#include "repository.h"
#include<algorithm>

class Service
{
private:
	repository repo;
public:
	vector<bills> getBills() const { return this->repo.getBills(); };
	vector<bills> getBillsSorted() const;
	double calculateAmountOfBillsFromCompany(string company);
};

