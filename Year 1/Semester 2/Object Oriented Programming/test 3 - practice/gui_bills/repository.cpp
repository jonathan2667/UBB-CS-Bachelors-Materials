#include "repository.h"

#include <iostream>

void repository::loadRepo()
{
	ifstream file("bills.txt");
	string line, companyName, code, sumString, isPaidString;
	double sum;
	bool isPaid;
	const char delimiter = '|';
	while (getline(file, line)) {
		istringstream iss(line);
		getline(iss, companyName, delimiter);
		getline(iss, code, delimiter);
		getline(iss, sumString, delimiter);
		getline(iss, isPaidString, delimiter);
		sum = stod(sumString);
		isPaid = isPaidString == "false" ? false : true;
		this->billsList.push_back(bills(companyName, code, sum, isPaid));
		cout << this->billsList.back().toString() << endl;
	}
}