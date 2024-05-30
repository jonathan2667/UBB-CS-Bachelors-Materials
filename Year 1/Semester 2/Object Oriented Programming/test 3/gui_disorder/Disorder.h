#pragma once
#include<string>
#include<iostream>
using namespace std;

class Disorder
{
private:
	string category, name, list;

public:

	Disorder(string category, string name, string list) : category(category), name(name), list(list) { ; };
	string getCategory() const{ return category; }
	string getName() const{ return name; }
	string getList() const{ return list; }
	string toString() { return category + " | " + name + " | " + list; }
	bool operator<(const Disorder& d) { return category < d.getCategory(); }

};

