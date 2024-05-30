#include <assert.h>
#include <exception>
#include <iostream>
#include "ExtendedTest.h"
#include "ListIterator.h"
#include "IteratedList.h"

using namespace std;

void testMixExtended() {
	cout << "Test mix" << endl;
	IteratedList list = IteratedList(); 
	assert(list.isEmpty());
	ListIterator it0 = list.first(); 
	assert(!it0.valid());
	try {
		it0.getCurrent(); 
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}

	list.addToEnd(1); 
	assert(list.size() == 1);
	ListIterator it = list.first();
	assert(it.getCurrent() == 1);

	ListIterator it2 = list.first(); 
	for (int i = 0; i < 100; i++) { 
		list.addToEnd(i);
		if (i <= 50) { 
			it2.next();
		}
		it.next();
		assert(it.getCurrent() == i); 
	} 
	assert(it2.getCurrent() == 50);
	assert(list.size() == 101);
	assert(it.valid());
	it.next(); 
	assert(!it.valid());
	try {
		list.getElement(it);
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}


	ListIterator it3 = list.search(50); 
	assert(it3.valid()); 
	assert(it3.getCurrent() == 50);
	TElem old = list.setElement(it3, 51);
	assert(old == 50);
	assert(it3.getCurrent() == it2.getCurrent()); 
	ListIterator it3_2 = list.search(50); 
	assert(!it3_2.valid());
	try {
		list.addToPosition(it3_2, 0);
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
	ListIterator it4 = list.search(99); 
	assert(it4.getCurrent() == 99);
	it4.next(); 
	assert(!it4.valid());
	try {
		it4.next();
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
	ListIterator it3_3 = list.search(51);
	list.addToPosition(it3_3, 150);
	assert(it3_3.getCurrent() == 150);

	ListIterator it5 = list.search(51);
	list.setElement(it5, 50);
	assert(list.getElement(it5) == 50);
	TElem old_2 = list.remove(it3_3); 
	assert(old_2 == 150);

	
	try {
		list.setElement(it, 0);
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
	try {
		list.remove(it);
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
}

void testIteratorSteps(IteratedList& l) {
	int count = 0;
	ListIterator it = l.first();
	while (it.valid()) {
		count++;
		it.next();
	}
	assert(count == l.size());
}

void testCreate() {
	cout << "Test create" << endl;
	IteratedList list = IteratedList();
	assert(list.isEmpty());
	ListIterator it = list.first();
	assert(!it.valid());
	try {
		it.next();
		assert(false);
	}
	catch (exception &) {
		assert(true);
	}
	assert(list.size() == 0);
}

ListIterator getIterator(int pos, IteratedList& list) {
	ListIterator it = list.first();
	int count = 0;
	while (count < pos)
	{
		it.next();
		count++;
	}
	return it;
}

void testAdd() {
	cout << "Test add" << endl;
	IteratedList list = IteratedList();
	list.addToEnd(1);
	assert(!list.isEmpty());
	assert(list.size() == 1);
	ListIterator it = list.first();
	assert(list.getElement(it) == 1);
	
	try {
		ListIterator it = getIterator(2, list);
		list.getElement(it);
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
	testIteratorSteps(list);
	for (int i = 0; i <= 100; i++) {
		list.addToEnd(i);
		ListIterator iter = getIterator(list.size() - 1, list);
		list.addToPosition(iter, i);
		try {
			ListIterator iter2 = getIterator((i + 2) * 2, list);
			list.addToPosition(iter2, i);
			assert(false);
		}
		catch (exception&) {
			assert(true);
		}
		testIteratorSteps(list);
		assert(list.size() == 2 * (i + 1) + 1);
	}
	ListIterator it2 = list.first();
	assert(it2.getCurrent() == 1);
	it2.next();
	int i = 0;
	while (it2.valid()) {
		assert(it2.getCurrent() == i);
		it2.next();
		assert(it2.getCurrent() == i);
		it2.next();
		i++;
	}
	assert(!it2.valid());
	try {
		it2.getCurrent();
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
	it2.first();
	assert(it2.valid());
	assert(it2.getCurrent() == 1);

	i = 1;
	int v = 0;
	while (i < list.size()) {
		ListIterator iter3 = getIterator(i, list);
		assert(list.getElement(iter3) == v);
		i++;
		i++;
		v++;
	}
	IteratedList list5 = IteratedList();
	int low = 100;
	int high = 102;
	while (list5.size() < 500) {
		list5.addToBeginning(low);
		low--;
		list5.addToEnd(high);
		high++;
	}
	ListIterator it5 = getIterator(249, list5);
	list5.addToPosition(it5, 101);
	ListIterator it6 = list5.first();
	int current = -149;
	while (it6.valid()) {
		assert(current == it6.getCurrent());
		current++;
		it6.next();
	}

}

void testSetRemoveSearch() {
	cout << "Test set, remove and search " << endl;
	IteratedList list = IteratedList();
	for (int i = 0; i <= 100; i++) {
		list.addToEnd(i);
	}
	assert(list.size() == 101);
	testIteratorSteps(list);
	assert(list.search(50).getCurrent() == 50);
	assert(list.search(100).getCurrent() == 100);
	ListIterator it1 = getIterator(100, list);
	assert(list.remove(it1) == 100);
	try {
		ListIterator it2 = getIterator(100, list);
		list.remove(it2);
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
	assert(list.size() == 100);
	try {
		assert(list.search(100).getCurrent() == -1);
		assert(false);
	}
	catch (exception& ex) {
		assert(true);
	}
	assert(list.search(99).getCurrent() == 99);
	int v = 99;
	for (int i = 0; i < 100; i++) {
		ListIterator it2 = getIterator(i, list);
		list.setElement(it2, v);
		v--;
	}
	ListIterator it3 = getIterator(99, list);
	assert(list.getElement(it3) == 0);
	assert(list.search(99).getCurrent() == 99);
	assert(list.search(0).getCurrent() == 0);
	assert(list.search(50).getCurrent() == 50);
	testIteratorSteps(list);
	
	ListIterator it = list.first();
	for (int i = 99; i > -1; i--) {
		assert(it.getCurrent() == i);
		it.next();
	}
	assert(!it.valid());
	for (int i = 99; i > -1; i--) {
		ListIterator it5 = getIterator(i, list);
		list.remove(it5);
		assert(list.size() == i);
	}
	assert(list.isEmpty());
	assert(list.size() == 0);
	it.first();
	assert(!it.valid());
}

void testQuantity() {
	cout << "Test quantity" << endl;
	IteratedList l1;
	int pos = 3;	
	for (int i = -10000; i <= 5000; i++) {
		if (l1.size() < 6) {
			l1.addToEnd(i);
		}
		else {
			ListIterator it = getIterator(pos, l1);
			l1.addToPosition(it, i);
			pos = (pos + 11) % l1.size();
		}
	}
	testIteratorSteps(l1);
	assert(l1.size() == 15001);
	for (int i = 0; i < l1.size(); i = i + 3) {
		ListIterator it = getIterator(i, l1);
		l1.remove(it);
	}
	testIteratorSteps(l1);
	for (int i = 0; i < 20000; i = i + 5) {
		l1.addToEnd(i);
	}
	testIteratorSteps(l1);

	IteratedList l2;
	pos = 1;
	for (int i = -100000; i <= 100000; i = i + 7) {
		if (l2.size() < 5) {
			l2.addToEnd(i);
		}
		else {
			ListIterator it = getIterator(pos, l2);
			l2.addToPosition(it, i);
			pos = (pos + 7) % l2.size();
		}
	}
	ListIterator listIt = l2.first();
	pos = 0;
	while (listIt.valid()) {
		TElem te = listIt.getCurrent();
		ListIterator it = getIterator(pos, l2);
		assert(l2.search(te).getCurrent() == te);
		assert(l2.search(te).getCurrent() == it.getCurrent());
		pos++;
		listIt.next();
	}
	for (int i = 0; i < l2.size(); i++) {
		ListIterator it = getIterator(i, l2);
		TElem elem = l2.getElement(it);
		assert(l2.search(elem).getCurrent() == it.getCurrent());
	}
	testIteratorSteps(l2);
	for (int i = -30000; i < 300000; i++) {
		ListIterator pos = l2.search(i);
		if (pos.valid()) {
			assert(l2.remove(pos) == i);
		}
	}
	testIteratorSteps(l2);
}

void compareListMinusPosition(IteratedList& l1, IteratedList& l2, int pos) {
	ListIterator it1 = l1.first();
	ListIterator it2 = l2.first();
	assert(l1.size() == l2.size() + 1);
	for (int i = 0; i < l2.size(); i++) {
		if (i != pos) {
			assert(l1.getElement(it1) == l2.getElement(it2));
		}
		else if (i == pos) {
			it1.next();
		}
		it1.next();
		it2.next();
	}

}

void testRemove() {
	cout << "Test remove" << endl;
	IteratedList list1;
	IteratedList list2;
	for (int i = 0; i < 100; i++) {
		list1.addToEnd(i);
		ListIterator it1 = getIterator(0, list1);
		list1.addToPosition(it1, 2 * i);
		list2.addToEnd(i);
		ListIterator it2 = getIterator(0, list2);
		list2.addToPosition(it2, 2 * i);
	}
	for (int i = 0; i < list1.size(); i++) {
		ListIterator it1 = getIterator(i, list1);
		ListIterator it2 = getIterator(i, list2);
		assert(list1.getElement(it1) == list2.getElement(it2));
	}

	int pos = 4;
	testIteratorSteps(list1);
	for (int i = 0; i < 50; i++) {
		ListIterator it = getIterator(pos, list2);
		list2.remove(it);
		compareListMinusPosition(list1, list2, pos);
		ListIterator it2 = getIterator(pos, list1);
		list1.remove(it2);
		pos = (pos + 7) % list2.size();
	}
	testIteratorSteps(list2);
	
}

void testAllExtended() {
	testCreate();
	testAdd();
	testSetRemoveSearch();//i
	testRemove();
	testMixExtended();
	testQuantity();
}


