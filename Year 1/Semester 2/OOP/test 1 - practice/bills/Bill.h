#pragma once
#include<string>
#include<iostream>
using namespace std;

struct Date {
    int day;
    int month;
    int year;

    Date(int d, int m, int y) : day(d), month(m), year(y) {}

    void toString() const {
        std::cout << day << "/" << month << "/" << year << std::endl;
    }

    bool operator==(const Date& other) const {
        return day == other.day && month == other.month && year == other.year;
    }

    bool operator<(const Date& other) const {
        if (year < other.year) return true;
        if (year > other.year) return false;
        if (month < other.month) return true;
        if (month > other.month) return false;
        return day < other.day;
    }

    bool operator>(const Date& other) const {
        if (year > other.year) return true;
        if (year < other.year) return false;
        if (month > other.month) return true;
        if (month < other.month) return false;
        return day > other.day;
    }
};

class Bill
{
private:
	string serialNumber, company;
    Date date;
    bool isPaid;
    double amount;
public:
    Bill(string serialNumber, string company, Date date, double amount, bool isPaid);
    
    string getSerialNumber() const;
    string toString() const;
    Date getDate() const;
    bool getIsPaid() const;
    double getAmount() const;
};

