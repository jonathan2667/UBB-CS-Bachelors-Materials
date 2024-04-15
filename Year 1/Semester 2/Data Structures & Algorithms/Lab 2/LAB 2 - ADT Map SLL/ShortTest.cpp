#include "ShortTest.h"
#include <assert.h>
#include "Map.h"
#include "MapIterator.h"

bool isNULL(TKey key) {
	return key == NULL_TVALUE;
}

void testAll() { //call each function to see if it is implemented
	Map m;
	assert(m.isEmpty() == true);
	assert(m.size() == 0); //add elements
	assert(m.add(5,5)==NULL_TVALUE);
	assert(m.add(1,111)==NULL_TVALUE);
	assert(m.add(10,110)==NULL_TVALUE);
	assert(m.add(7,7)==NULL_TVALUE);
	assert(m.add(1,1)==111);
	assert(m.add(10,10)==110);
	assert(m.add(-3,-3)==NULL_TVALUE);
	assert(m.size() == 5);
	assert(m.search(10) == 10);
	assert(m.search(16) == NULL_TVALUE);
	assert(m.remove(1) == 1);
	assert(m.remove(6) == NULL_TVALUE);
	assert(m.size() == 4);

	
	TElem e;
	MapIterator id = m.iterator();
	id.first();
	int s1 = 0, s2 = 0;
	while (id.valid()) {
		e = id.getCurrent();
		s1 += e.first;
		s2 += e.second;
		id.next();
	}
	assert(s1 == 19);
	assert(s2 == 19);
	

	
	Map m1;
	m1.add(-111111, -111111); //bun
	m1.add(-1, -1);
	m1.add(1, -111111); 
	m1.add(0, 0);
	m1.add(-5, -111111); 
	m1.add(3, 3); 

	
	assert(m1.size() == 6); 
	m1.filter(isNULL);
	assert(m1.size() == 1);
	MapIterator it1 = m1.iterator();
	it1.first();
	int keySum1 = 0, valueSum1 = 0;
	while (it1.valid()) {
		TElem e = it1.getCurrent();
		keySum1 += e.first;
		valueSum1 += e.second;
		it1.next();
	}
	assert(keySum1 == -111111);
	assert(valueSum1 == -111111);
}


