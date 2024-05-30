#include "ShortTest.h"
#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <assert.h>
#include <vector>
#include<iostream>

void testAll() {
	MultiMap m;
	m.add(1, 100);
	m.add(2, 200);
	m.add(3, 300);
	m.add(1, 500);
	m.add(2, 600);
	m.add(4, 800);

	assert(m.size() == 6);

	assert(m.remove(5, 600) == false);
	assert(m.remove(1, 500) == true);

	assert(m.size() == 5);

    vector<TValue> v;
	v=m.search(6);
	assert(v.size()==0);

	v=m.search(1);
	assert(v.size()==1);

	assert(m.isEmpty() == false);

	
	MultiMapIterator im = m.iterator();
	assert(im.valid() == true);
	while (im.valid()) {
		im.getCurrent();
		im.next();
	}
	assert(im.valid() == false);
	im.first();
	assert(im.valid() == true);
	

	//test addIfNotPresent(MultiMap& m)
	MultiMap m2;

	m2.add(1, 100);
	m2.add(2, 200);
	m2.add(3, 300);
	m2.add(4, 400);

	assert(m2.size() == 4);

	MultiMap m3;
	m3.add(1, 100);
	//m3.add(2, 200);
		
	assert(m3.size() == 1);

	assert(m3.addIfNotPresent(m2) == 3);
}
