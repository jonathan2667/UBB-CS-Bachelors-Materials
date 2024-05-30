#include "ShortTest.h"

#include <assert.h>
#include <exception>


#include "IteratedList.h"
#include "ListIterator.h"

using namespace std;

void test_removeBetween() {
	IteratedList list;

	try {
		IteratedList emptyList;
		ListIterator start = emptyList.first();
		ListIterator end = emptyList.first();
		emptyList.removeBetween(start, end);
	}
	catch (std::exception& e) {
		assert(true);
	}

	for (int i = 0; i < 10; i++) {
		list.addToEnd(i);
	}

	ListIterator startSingle = list.first();
	ListIterator endSingle = startSingle;
	endSingle.next();
	int expectedSizeAfterSingleRemove = list.size() - 1;
	list.removeBetween(startSingle, endSingle);
	assert(list.size() == expectedSizeAfterSingleRemove);
}


void testAll() {
	IteratedList list = IteratedList();
	assert(list.size() == 0);
	assert(list.isEmpty());

	list.addToEnd(1);
	assert(list.size() == 1);
	assert(!list.isEmpty());

	ListIterator it = list.search(1);
	assert(it.valid());
	assert(it.getCurrent() == 1);
	it.next();
	assert(!it.valid());
	it.first();
	assert(it.valid());
	assert(it.getCurrent() == 1);

	assert(list.remove(it) == 1);
	assert(list.size() == 0);
	assert(list.isEmpty());

	list.addToEnd(1);
	list.addToEnd(3);
	list.addToEnd(7);
	ListIterator it3 = list.first();
	list.addToPosition(it3, 77);
	list.addToPosition(it3, 44);
	assert(list.size() == 5);
	ListIterator it2 = list.first();
	assert(it2.getCurrent() == 1);
	it2.next();

	assert(it2.getCurrent() == 77);
	it2.next();
	assert(it2.getCurrent() == 44);
	it2.next();
	assert(it2.getCurrent() == 3);
	it2.next();
	assert(it2.getCurrent() == 7);
	it2.next();
	assert(it2.valid() == false);

	IteratedList list2 = IteratedList();
	list2.addToBeginning(4);
	list2.addToEnd(5);
	list2.addToBeginning(3);
	list2.addToEnd(6);
	list2.addToBeginning(2);
	list2.addToEnd(7);
	int i = 2;
	ListIterator it4 = list2.first();
	while (it4.valid()) {
		assert(it4.getCurrent() == i);
		i++;
		it4.next();
	}


	


}


