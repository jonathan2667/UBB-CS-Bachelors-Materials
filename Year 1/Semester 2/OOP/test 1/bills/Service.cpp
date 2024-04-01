#include "Service.h"
#include<algorithm>

Service::Service() {
}

void Service::addBill(Bill b) {
	//adds a bill to the current list in the repository
	this->repo.addBill(b);
}


vector<Bill> Service::getBillsSortedByCompanyName() {
		vector<Bill> allBills = this->repo.getBills();
		sort(allBills.begin(), allBills.end(), [](Bill b1, Bill b2) {
		return b1.getCompany() < b2.getCompany();
	});
	return allBills;
}

vector<Bill> Service::sortPaidBills() {
	vector<Bill> allBills = this->repo.getBills();
	vector<Bill> paidBills;
	for (Bill b : allBills) {
		if (b.getIsPaid() == true) {
			paidBills.push_back(b);
		}
	}
	sort(paidBills.begin(), paidBills.end(), [](Bill b1, Bill b2) {
		return b1.getCompany() < b2.getCompany();
	});
	return paidBills;
}

double Service::calculateTotalAmount() {
	//calculates the total amount of all paid bills
	vector<Bill> allBills = sortPaidBills();
	double sum = 0;
	for (Bill b : allBills) {
		sum += b.getAmount();
	}
	return sum;
}