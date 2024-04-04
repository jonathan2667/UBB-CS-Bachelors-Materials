#pragma once
#include "Service.h"
#include <iostream>
#include <string>
#include <vector>

class Ui
{
private:
	Service service = Service();
public:
	Ui();
	void printMenu();
	void run();

	void removeBill();
	void showAllBills();
	void sortUnpaidBills();
	void calculateTotalAmount();

};

