#pragma once
#include<string>
using namespace std;

class Department
{
};

class Building {
public:
	string address;
	int constructionYear;
	Building(string address, int constructionYear) : address{ address }, constructionYear{ constructionYear } {};
	virtual string toString();
	virtual bool canBeDemolished() { return false; };
	virtual bool mustBeRestored() { return false; };
};

class Flats : public Building {
public:
	int nrApp;
	int occupiedApp;
	
	Flats(string address, int constructionYear, int nrApp, int occupiedApp) :
		Building{ address, constructionYear }, nrApp{ nrApp }, occupiedApp{ occupiedApp } {};
	string toString();
	bool canBeDemolished();
	bool mustBeRestored();
};

class House : public Building {
public:
	string type;
	bool isHistorical;

	House(string address, int constructionYear, string type, bool isHistorical) :
		Building{ address, constructionYear }, type{ type }, isHistorical{ isHistorical } {};
	string toString();
	bool canBeDemolished();
	bool mustBeRestored();
};