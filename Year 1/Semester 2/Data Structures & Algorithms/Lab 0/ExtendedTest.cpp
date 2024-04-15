#include "ExtendedTest.h"
#include "FixedCapBiMap.h"
#include "FixedCapBiMapIterator.h"

#include <assert.h>
#include <iostream>

using namespace std;

void testIteratorSteps(FixedCapBiMap& m) {
	FixedCapBiMapIterator mi = m.iterator();
	int count = 0;
	while (mi.valid()) {
		count++;
		mi.next();
	}
	assert(count == m.size());
}

void testCreate() {
	cout << "Test create" << endl;
	FixedCapBiMap m(10);
	assert(m.size() == 0);
	assert(m.isEmpty() == true);

	ValuePair empty = std::pair<TValue, TValue>(NULL_TVALUE, NULL_TVALUE);

	for (int i = -10; i < 10; i++) { 
		assert(m.search(i) == empty);
	}
	for (int i = -10; i < 10; i++) { 
		assert(m.search(i) == empty);
	}

	FixedCapBiMapIterator it = m.iterator(); 
	assert(it.valid() == false);
	try {
		it.next();
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
	try {
		it.getCurrent();
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
}


void testAdd() {
	cout << "Test add" << endl;
	
	FixedCapBiMap m(50); 

	for (int i = 0; i < 10; i++) {
		assert(m.add(i, i) == true);
	}
	assert(m.isEmpty() == false);
	assert(m.size() == 10);
	for (int i = -10; i < 0; i++) {
		assert(m.add(i, i) == true);
	}
	for (int i = 0; i < 10; i++) { 
		assert(m.add(i, i) == true);
	}
	for (int i = 10; i < 20; i++) { 
		assert(m.add(i, i) == true);
	}
	assert(m.isEmpty() == false);
	assert(m.size() == 40);
	
	FixedCapBiMap m2(21000);
	for (int i = -100; i < 100; i++) { 
		m2.add(i, i);
	}
	assert(m2.isEmpty() == false);
	assert(m2.size() == 200);
	ValuePair empty = std::pair<TValue, TValue>(NULL_TVALUE, NULL_TVALUE);
	for (int i = -200; i < 200; i++) {
		if (i < -100) {
			assert(m2.search(i) == empty);
		}
		else if (i < 0) {
			ValuePair one = std::pair<TValue, TValue>(i, NULL_TVALUE);
			assert(m2.search(i) == one);
		}
		else if (i < 100) {
			ValuePair one = std::pair<TValue, TValue>(i, NULL_TVALUE);
			assert(m2.search(i) == one);
		}
		else {
			assert(m2.search(i) == empty);
		}
	}
	for (int i = 10000; i > -10000; i--) { 
		m2.add(i, i);
	}
	testIteratorSteps(m2);
	assert(m2.size() == 20200);

	for (int i = -100; i < 100; i++) {
		assert(m2.add(i, i) == false);
	}
	assert(m2.size() == 20200);
}


void testRemove() {
	cout << "Test remove" << endl;
	FixedCapBiMap m(1000);

	for (int i = -100; i < 100; i++) { 
		assert(m.remove(i, i) == false);
	}
	assert(m.size() == 0);
	for (int i = -100; i < 100; i = i + 2) { 
		assert(m.add(i, i) == true);
	}
	for (int i = -100; i < 100; i++) { 
		if (i % 2 == 0) {
			assert(m.remove(i, i) == true);
		}
		else {
			assert(m.remove(i, i) == false);
		}
	}
	assert(m.size() == 0);

	for (int i = -100; i <= 100; i = i + 2) { 
		assert(m.add(i, i) == true);
	}
	testIteratorSteps(m);
	for (int i = 100; i > -100; i--) { 
		if (i % 2 == 0) {
			assert(m.remove(i, i) == true);
		}
		else {
			assert(m.remove(i, i) == false);
		}
		testIteratorSteps(m);
	}

	assert(m.size() == 1);

	m.remove(-100, -100);
	assert(m.size() == 0);

	for (int i = -100; i < 100; i++) {
		assert(m.add(i, 0) == true);
		assert(m.add(i, 1) == true);
		assert(m.add(i, 2) == false);
		assert(m.add(i, 3) == false);
		assert(m.add(i, 4) == false);
	}
	assert(m.size() == 400);
	for (int i = -200; i < 200; i++) { 
		if (i < -100 || i >= 100) {
			assert(m.remove(i, 0) == false);
		}
		else {
			assert(m.remove(i, 0) == true);
			assert(m.remove(i, 1) == true);
		}
	}
	assert(m.size() == 0);

}



void testIterator() {
	cout << "Test iterator" << endl;
	FixedCapBiMap m(100);
	FixedCapBiMapIterator it = m.iterator(); 
	assert(it.valid() == false);
	   
	for (int i = 0; i < 100; i++) { 
		m.add(33, 33);
	}
	FixedCapBiMapIterator it2 = m.iterator(); 
	assert(it2.valid() == true);
	TElem el = it2.getCurrent();
	assert(el.first == 33);
	assert(el.second == 33);
	it2.next();
	el = it2.getCurrent();
	assert(el.first == 33);
	assert(el.second == 33);
	it2.next();
	assert(it2.valid() == false);
	try {
		it2.next();
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}
	try {
		it2.getCurrent();
		assert(false);
	}
	catch (exception&) {
		assert(true);
	}

	it2.first();
	assert(it2.valid() == true);

	FixedCapBiMap m2(500);
	for (int i = -100; i < 100; i++) { 
		assert(m2.add(i, i) == true);
		assert(m2.add(i, i) == true);
		assert(m2.add(i, i) == false);
	}
	FixedCapBiMapIterator it3 = m2.iterator();
	assert(it3.valid() == true);
	for (int i = 0; i < 400; i++) {
		it3.next();
	}
	assert(it3.valid() == false);
	it3.first();
	assert(it3.valid() == true);

	FixedCapBiMap m3(300);
	for (int i = 0; i < 200; i = i + 4) { 
		m3.add(i, i);
	}

	FixedCapBiMapIterator it4 = m3.iterator();
	assert(it4.valid() == true);
	int count = 0;
	while (it4.valid()) {
		TElem e = it4.getCurrent();
		assert(e.first % 4 == 0);
		it4.next();
		count++;
	}
	assert(count == 50);

}



void testQuantity() {
	FixedCapBiMap m(61000);
	cout << "Test quantity" << endl;
	for (int j = 0; j < 30000; j = j + 1) {
		assert(m.add(j, j) == true);
	}
	for (int i = 10; i >= 1; i--) {
		for (int j = 0; j < 30000; j = j + 1) {
			if (i == 10) {
				assert(m.add(j, j) == true);
			}
			else {
				assert(m.add(j, j) == false);
			}
		}
	}
	assert(m.size() == 60000);
	FixedCapBiMapIterator it = m.iterator();
	assert(it.valid() == true);
	for (int i = 0; i < m.size(); i++) {
		it.next();
	}
	it.first();
	while (it.valid()) {
		TElem e = it.getCurrent();
		ValuePair val = std::pair<TValue, TValue>(e.first, e.first);
		assert(m.search(e.first) == val);
		it.next();
	}
	assert(it.valid() == false);
	
	for (int j = 30000 - 1; j >= 0; j--) {
		assert(m.remove(j, j) == true);
		assert(m.remove(j, j) == true);
	}
	for (int i = 0; i < 10; i++) {
		for (int j = 40000; j >= -4000; j--) {
			assert(m.remove(j, j) == false);
		}
	}
	assert(m.size() == 0);
}

void testCapacity() {
	cout << "Test capacity" << endl;
	FixedCapBiMap m(10);
	for (int i = 0; i < 10; i++) {
		assert(m.add(i, i)== true);
	}
	assert(m.isFull() == true);
	try {
		m.add(11, 11);
		assert(false);
	}
	catch (exception& ) {
		assert(true);
	}
	for (int i = 0; i < 2; i++) {
		assert(m.remove(i, i) == true);
	}
	assert(m.isFull() == false);
	assert(m.add(2, 2) == true);
	assert(m.add(2, 2) == false);
	assert(m.add(1, 1) == true);
	assert(m.isFull() == true);
	for (int i = 0; i < 10; i++) {
		try {
			m.add(10, 10);
			assert(false);
		}
		catch (exception&) {
			assert(true);
		}
		assert(m.isFull() == true);
	}
}

void testSearch() {
	cout << "Test search" << endl;
	FixedCapBiMap m(100);
	ValuePair empty = std::pair<TValue, TValue>(NULL_TVALUE, NULL_TVALUE);
	for (int i = 0; i < 100; i++) {
		assert(m.search(i) == empty);
	}
	for (int i = 0; i < 50; i++) {
		m.add(i, i);
	}
	for (int i = 0; i < 50; i++) {
		ValuePair one = std::pair<TValue, TValue>(i, NULL_TVALUE);
		assert(m.search(i) == one);
	}
	for (int i = 0; i < 50; i++) {
		m.add(i, i+2);
	}
	for (int i = 0; i < 50; i++) {
		ValuePair one = std::pair<TValue, TValue>(i, i+2);
		ValuePair two = std::pair<TValue, TValue>(i + 2, i );
		assert(m.search(i) == one || m.search(i) == two);
	}
	for (int i = 0; i <50; i++) {
		assert(m.remove(i, i ) == true);
	}
	for (int i = 0; i < 50; i++) {
		ValuePair one = std::pair<TValue, TValue>(i + 2, NULL_TVALUE);
		assert(m.search(i) == one);
	}
	for (int i = 0; i < 50; i++) {
		assert(m.remove(i, i + 2) == true);
	}
	for (int i = 0; i < 50; i++) {
		assert(m.search(i) == empty);
	}
}

void testAllExtended() {
	testCreate();
	testAdd();
	testRemove();
	testIterator();
	testSearch();
	testCapacity();
	testQuantity();
}




