#include "service.h"
#include<algorithm>

vector<bills> Service::getBillsSorted() const
{
	vector<bills> allBills = this->repo.getBills();
	sort(allBills.begin(), allBills.end());
	return allBills;
}

double Service::calculateAmountOfBillsFromCompany(string company)
{
	vector<bills> allBills = this->repo.getBills();
	double amount = 0;
	for (auto bill : allBills)
		if (bill.getCompanyName() == company and !bill.getIsPaid())
			amount += bill.getSum();
	return amount;
}

