#include "Bill.h"
#include <sstream>

Bill::Bill(string serialNumber, string company, Date date, double amount, bool isPaid) : serialNumber(serialNumber), company(company), date(date), amount(amount), isPaid(isPaid) {
}

string Bill::getSerialNumber() const {
	return serialNumber;
}

Date Bill::getDate() const {
	return date;
}

bool Bill::getIsPaid() const {
	return isPaid;
}

double Bill::getAmount() const {
	return amount;
}

string Bill::toString() const {
	ostringstream oss;
	oss << "Serial Number: " << serialNumber << " | Company: " << company << " | Date: " << date.day << "." << date.month << "." << date.year << " | Amount: " << amount << " | Paid: " << (isPaid ? "Yes" : "No");
	return oss.str();
}