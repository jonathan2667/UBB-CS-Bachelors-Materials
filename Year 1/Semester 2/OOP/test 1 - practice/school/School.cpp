#include "School.h"
#include <sstream>


School::School(string name, pair<float, float> location, string date, bool schoolWasVisited)
{
	this->name = name;
	this->location = location;
	this->date = date;
	this->schoolWasVisited = schoolWasVisited; 
}

string School::getName() const
{
	return name;
}

pair<float, float> School::getLocation() const
{
	return location;
}

string School::getDate() const
{
	return date;
}

bool School::getSchoolWasVisited() const
{
	return schoolWasVisited;
}

void School::setSchoolWasVisited(bool schoolWasVisited)
{
	this->schoolWasVisited = schoolWasVisited;
}

void School::setDate(string date)
{
	this->date = date;
}

void School::setLocation(pair<float, float> location)
{
		this->location = location;
}

void School::setName(string name)
{
	this->name = name;
}

string School::toString() const
{
	stringstream ss;
	ss << "Name: " << name << " Location: " << location.first << " " << location.second << " Date: " << date << " School was visited: " << schoolWasVisited;
	return ss.str();
}