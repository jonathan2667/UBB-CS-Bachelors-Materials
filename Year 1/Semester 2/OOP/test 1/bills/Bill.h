#pragma once
#include<string>
#include<iostream>
using namespace std;


class Bill
{
private:
	string serialNumber, company;
    bool isPaid;
    double amount;
public:
    Bill(string serialNumber, string company, double amount, bool isPaid);
    
    string getSerialNumber() const;
    string toString() const;
    bool getIsPaid() const;
    double getAmount() const;
    string getCompany() const;
};

