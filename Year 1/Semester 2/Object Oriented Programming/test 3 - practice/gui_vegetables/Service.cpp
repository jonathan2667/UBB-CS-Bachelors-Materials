#include "Service.h"

vector<Vegetables> Service::getAllVegetables(){
	vector<Vegetables> all = repository.getAllVegetables();
	sort(all.begin(), all.end());
	return all;
}

vector<string>  Service::getAllUniqueFamilies() {
	ofstream fout("test.txt");

	vector<Vegetables> all = repository.getAllVegetables();
	sort(all.begin(), all.end());
	vector<string> allfinal;

	for (int i = 0; i < all.size(); i++) {
		bool found = 0;
		for (int j = 0; j < allfinal.size(); j++)
			if (all[i].getFamily() == allfinal[j]) found = 1;
	
		if (!found) {
			allfinal.push_back(all[i].getFamily());
			fout << all[i].toString();
		}
	}
	return allfinal;
}

vector<Vegetables> Service::getAllVegetablesBelongingToFamily(string family) {
	vector<Vegetables> all = repository.getAllVegetables();
	vector<Vegetables> allfinal;

	for (auto x : all)
		if (x.getFamily() == family) allfinal.push_back(x);

	return allfinal;
}

Vegetables Service::getVegetableFromName(string name) {
	vector<Vegetables> all = repository.getAllVegetables();
	for (auto x : all)
		if (x.getName() == name) return x;
	return Vegetables("none", "none", "None");
}