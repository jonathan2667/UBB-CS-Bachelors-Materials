#include "Ui.h"
#include <iostream>
#include "Tests.h"


using namespace std;

Ui::Ui() {
	;
}
void Ui::printMenu() {
    cout << "1. Add a bill\n";
    cout << "2. Show all bills\n";
    cout << "3. Show paid bills (sorted) & Calculate total amount of unpaid bills\n";
}

void Ui::run() {
    while (true) {
        printMenu();
		int command;
		cout << "Enter command: ";
		cin >> command;
		if (command == 1) {
			addBill();
		} else if (command == 2) {
			showAllBills();
		} else if (command == 3) {
			sortPaidBills();
			calculateTotalAmount();
		} else if (command == 4) {
			;
		}
		else {
			break;
		}
    }
}

void Ui::calculateTotalAmount() {
	double totalAmount = service.calculateTotalAmount();
	cout << "Total amount of unpaid bills: " << totalAmount << endl;
}

void Ui::sortPaidBills() {
	vector<Bill> bills = service.sortPaidBills();
	for (Bill& bill : bills) {
		cout << bill.toString() << endl;
	}
}

void Ui::addBill() {
	string serialNumber;
	cout << "Enter serial number: ";
	cin >> serialNumber;

	string company;
	cout << "Enter company: ";
	cin >> company;
	
	double amount;
	cout << "Enter amount: ";
	cin >> amount;

	bool isPaid;
	cout << "Is the bill paid? (1/0): ";
	cin >> isPaid;

	try {
		service.addBill(Bill(serialNumber, company, amount, isPaid));
		cout << "Bill added successfully\n";
	}
	catch (exception& e) {
		cout << e.what() << endl;
	}
}

void Ui::showAllBills() {
	vector<Bill> bills = service.getBillsSortedByCompanyName();
	for (Bill& bill : bills) {
		cout << bill.toString() << endl;
	}
}


int main()
{
	testAll();


	Ui ui = Ui();
	ui.run();
	return 0;
}