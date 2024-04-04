#include "Bill.h"
#include <sstream>

Bill::Bill(string serialNumber, string company, double amount, bool isPaid) : serialNumber(serialNumber), company(company), amount(amount), isPaid(isPaid) {
}

string Bill::getSerialNumber() const {
	return serialNumber;
}

bool Bill::getIsPaid() const {
	return isPaid;
}

double Bill::getAmount() const {
	return amount;
}

string Bill::toString() const {
	ostringstream oss;
	oss << "Serial Number: " << serialNumber << " | Company: " << company << " | Amount: " << amount << " | Paid: " << (isPaid ? "Yes" : "No");
	return oss.str();
}

string Bill::getCompany() const {
	return company;
}