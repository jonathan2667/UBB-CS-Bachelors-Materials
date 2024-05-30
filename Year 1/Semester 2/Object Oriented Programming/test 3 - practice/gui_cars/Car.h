#pragma once
#include<string>
#include<iostream>

using namespace std;

class Car
{
private:
	string manufacturer, model, color;
	int year;
public:
	Car(string manufacturer, string model, string color, int year) : manufacturer(manufacturer), model(model), color(color), year(year) {}
	string getManufacturer() const { return manufacturer; }
	string getModel() const { return model; }
	string getColor() const { return color; }
	string toString() const { return manufacturer + " " + model + " " + color + " " + to_string(year); }
	int getYear() const { return year; }
	bool operator<(const Car& c) const { return manufacturer < c.getManufacturer(); }
	

};

