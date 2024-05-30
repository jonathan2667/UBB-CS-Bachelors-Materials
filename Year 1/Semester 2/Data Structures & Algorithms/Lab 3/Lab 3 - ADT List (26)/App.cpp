#include <iostream>
#include "ShortTest.h"
#include "ExtendedTest.h"

int main() {
	test_removeBetween();
	testAll();
	testAllExtended();
	std::cout << "Finished LP Tests!" << std::endl;
	system("pause");
}
