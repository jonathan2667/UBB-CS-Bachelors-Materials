#pragma once
#include<string> 

using namespace std;


class bills
{
private:
	string companyName, code;
	double sum;
	bool isPaid;

public:
	bills(string companyName = "", string code = "", double sum = 0, bool isPaid = false) :
		companyName(companyName), code(code), sum(sum), isPaid(isPaid) {};

	string getCompanyName() const { return this->companyName; };
	string getCode() const { return this->code; };
	double getSum() const { return this->sum; };
	bool getIsPaid() const { return this->isPaid; };

	string toString() const {
		string isPaid = this->isPaid ? "Paid" : "Not paid";
		return "Company name: " + this->companyName + ", Code: " + this->code + ", Sum: " + to_string(this->sum) + ", " + isPaid;
	}

	inline bool operator<(const bills& other) const {
		return this->companyName < other.getCompanyName();
	}
};

