#include "Repo.h"
#include "Bill.h"

Repo::Repo() {
	addBill(Bill("OA223X", "Digi", 123.23, false));
	addBill(Bill("1A223X", "Orange", 143.21, true));
	addBill(Bill("2A223X", "NVN", 153.92, false));
	addBill(Bill("3A223X", "CBC", 173.82, false));
	addBill(Bill("4A223X", "RDS", 183.78, true));
	addBill(Bill("5A223X", "Vodafone", 193.12, false));
	addBill(Bill("6A223X", "Telekom", 203.12, true));
}

void Repo::addBill(Bill b) {
	//adds bill to the list, if already one with same serial number, throws exception
	for (Bill bill : this->bills) {
		if (bill.getSerialNumber() == b.getSerialNumber()) {
			throw exception("Bill with same serial number already exists");
		}
	}
	this->bills.push_back(b);
}

vector<Bill> Repo::getBills() {
	return this->bills;
}