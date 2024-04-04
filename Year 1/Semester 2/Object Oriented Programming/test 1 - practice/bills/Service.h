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
	void removeBill(string serialNumber);
	vector<Bill> getBills();
	vector<Bill> getUnpaidBillsSorted();
	double calculateTotalAmount();
};

