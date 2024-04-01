#pragma once

#include <string>
#include <sstream>
#include <tuple>

using namespace std;

class School
{
private:
	string name;
	pair<float, float> location;
	string date;
	bool schoolWasVisited;
	tuple<int, int, int> parseDate(const std::string& dateStr) const {
		std::istringstream iss(dateStr);
		int day, month, year;
		char delimiter; 
		iss >> day >> delimiter >> month >> delimiter >> year;
		return { year, month, day }; 
	}

public:
	School();
	School(string name, pair<float, float> location, string date, bool schoolWasVisited);
	//~School();

	string getName() const;
	pair<float, float> getLocation() const;
	string getDate() const;
	bool getSchoolWasVisited() const;

	void setName(string name);
	void setLocation(pair<float, float> location);
	void setDate(string date);
	void setSchoolWasVisited(bool schoolWasVisited);

	string toString() const;

	bool isDateAfter(const std::string& otherDate) const {
		return parseDate(this->date) > parseDate(otherDate);
	}

	bool isDateBefore(const std::string& otherDate) const {
		return parseDate(this->date) < parseDate(otherDate);
	}
	
};

