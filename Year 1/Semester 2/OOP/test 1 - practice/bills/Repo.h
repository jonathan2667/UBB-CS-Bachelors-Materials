#pragma once
#include<vector>
#include "Bill.h"
using namespace std;

class Repo
{
private:
	vector<Bill> bills;

public:
	Repo();

	void addBill(Bill b);
	void removeBill(string serialNumber);
	vector<Bill> getBills();

};

