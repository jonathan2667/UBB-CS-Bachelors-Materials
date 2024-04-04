#pragma once
#include "Repo.h"
#include "Bill.h"

class Service
{
private:
	Repo repo = Repo();

public:
	Service();
	void addBill(Bill b);
	vector<Bill> getBillsSortedByCompanyName();
	vector<Bill> sortPaidBills();
	double calculateTotalAmount();
};

