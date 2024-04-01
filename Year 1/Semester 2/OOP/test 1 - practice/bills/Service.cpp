#include "Service.h"
#include<algorithm>

Service::Service() {
}

void Service::addBill(Bill b) {
	this->repo.addBill(b);
}

void Service::removeBill(string serialNumber) {
	this->repo.removeBill(serialNumber);
}

vector<Bill> Service::getBills() {
	return this->repo.getBills();
}

vector<Bill> Service::getUnpaidBillsSorted() {
	vector<Bill> allBills = this->repo.getBills();
	vector<Bill> unpaidBills;
	for (Bill b : allBills) {
		if (b.getIsPaid() == false) {
			unpaidBills.push_back(b);
		}
	}
	sort(unpaidBills.begin(), unpaidBills.end(), [](Bill b1, Bill b2) {
		return b1.getDate() < b2.getDate();
	});
	return unpaidBills;
}

double Service::calculateTotalAmount() {
	vector<Bill> allBills = this->repo.getBills();
	double sum = 0;
	for (Bill b : allBills) {
		sum += b.getAmount();
	}
	return sum;
}