#pragma once
#include<string>
#include<iostream>
#include<fstream>
using namespace std;

class Vegetables
{
private:
	string family, name, list;

public:
	Vegetables(string family, string name, string list) : family(family), name(name), list(list) { ; };
	string getFamily() const { return family; }
	string getName() const { return name; }
	string getList() const { return list; }
	bool operator <(const Vegetables& v) { return family < v.getFamily(); }
	string toString() { return name + " | " + list; }
};

