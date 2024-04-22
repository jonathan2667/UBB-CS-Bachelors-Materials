#include "Applicance.h"

string Appliance::toString() {
	return "Id:\n" + id +  '\n';
}

string Refrigerator::toString() {
	return "Refrigerator\n" + Appliance::toString() + "electricityUsageClass\n" +
		electricityUsageClass + "\nhasFreezer\n" + to_string(hasFreezer) + '\n';
}

string DishWasher::toString() {
	return "DishWasher\n" + Appliance::toString() + "consumedElectricityForOneHour\n" + to_string(consumedElectricityForOneHour) + '\n';
}

double Refrigerator::consumedElectricity() {
	double total = 0;
	if (hasFreezer) total = 20;
	if (electricityUsageClass == "A") total += 30 * 3;
	if (electricityUsageClass == "A+") total += 30 * 2.5;
	if (electricityUsageClass == "A++") total += 30 * 2;
	return total;
}

double DishWasher::consumedElectricity() {
	return 20 * consumedElectricityForOneHour;
}