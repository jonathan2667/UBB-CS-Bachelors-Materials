#include "Service.h"
#include<algorithm>
#include<cstring>
#include<fstream>

vector<Disorder> Service::getAllDisorders() {
	vector<Disorder> disorders = repository.getDisorders();
	sort(disorders.begin(), disorders.end());
	return disorders;
}

vector<string> Service::getAllSymptomsFromName(string name) {
	ofstream fout("test.txt");
	vector<Disorder> disorders = repository.getDisorders();
	string allSymptoms = "";
	for (auto d : disorders) {
		if (d.getName() == name) allSymptoms = d.getList();
	}


	vector<string> result;
	int startIndex = 0;
	for (int i = 0; i < allSymptoms.size(); i++) {
		if (allSymptoms[i] == ',') {
			if (startIndex == 0)
				result.push_back(allSymptoms.substr(startIndex, i));
			else result.push_back(allSymptoms.substr(startIndex + 1, i));
			fout << allSymptoms.substr(startIndex, i) << endl;
			startIndex = i;
		}
	}
	if (startIndex != allSymptoms.size()) result.push_back(allSymptoms.substr(startIndex + 1, allSymptoms.size()));
	return result;
}