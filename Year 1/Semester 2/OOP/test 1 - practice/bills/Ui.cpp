#include "Ui.h"
#include <iostream>
using namespace std;

Ui::Ui() {
	;
}
void Ui::printMenu() {
    cout << "1. Remove a bill\n";
    cout << "2. Show all bills\n";
    cout << "3. Sort unpaid bills by due date\n";
    cout << "4. Calculate total amount of unpaid bills\n";
}

void Ui::run() {
    while (true) {
        printMenu();
		int command;
		cout << "Enter command: ";
		cin >> command;
		if (command == 1) {
			removeBill();
		} else if (command == 2) {
			showAllBills();
		} else if (command == 3) {
			sortUnpaidBills();
		} else if (command == 4) {
			calculateTotalAmount();
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

void Ui::sortUnpaidBills() {
	vector<Bill> bills = service.getUnpaidBillsSorted();
	for (Bill& bill : bills) {
		cout << bill.toString() << endl;
	}
}

void Ui::removeBill() {
	string serialNumber;
	cout << "Enter serial number: ";
	cin >> serialNumber;
	try {
		service.removeBill(serialNumber);
		cout << "Bill removed successfully\n";
	}
	catch (exception& e) {
		cout << e.what() << endl;
	}
}

void Ui::showAllBills() {
	vector<Bill> bills = service.getBills();
	for (Bill& bill : bills) {
		cout << bill.toString() << endl;
	}
}


int main()
{
	Ui ui = Ui();
	ui.run();
	return 0;
}