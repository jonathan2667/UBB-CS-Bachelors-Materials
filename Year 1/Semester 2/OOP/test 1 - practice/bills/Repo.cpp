#include "Repo.h"
#include "Bill.h"

Repo::Repo() {
	addBill(Bill("OA223X", "Digi Sport", Date(12, 5, 2022), 123, false));
	addBill(Bill("1A223X", "Orange Sport", Date(13, 5, 2022), 143, true));
	addBill(Bill("2A223X", "NVN Sport", Date(14, 5, 2017), 153, false));
	addBill(Bill("3A223X", "CBC Sport", Date(15, 5, 2022), 173, false));
	addBill(Bill("4A223X", "RDS Sport", Date(16, 5, 2021), 183, true));
}

void Repo::addBill(Bill b) {
	this->bills.push_back(b);
}

void Repo::removeBill(string serialNumber) {
	bool found = false;
	vector<Bill>::iterator it;
	it = find_if(this->bills.begin(), this->bills.end(), [serialNumber](Bill b) {return b.getSerialNumber() == serialNumber; });
	if (it != this->bills.end()) {
		this->bills.erase(it);
		found = true;
	}
	if (found == false) {
		throw exception("The bill does not exist!");
	}
}

vector<Bill> Repo::getBills() {
	return this->bills;
}