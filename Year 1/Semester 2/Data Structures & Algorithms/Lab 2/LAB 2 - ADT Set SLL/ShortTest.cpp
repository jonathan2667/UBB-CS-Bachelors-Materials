#include "ShortTest.h"
#include <assert.h>
#include "Set.h"
#include "SetIterator.h"

void testAll() { 
	Set s;
	assert(s.isEmpty() == true);
	assert(s.size() == 0); 
	assert(s.add(5)==true);
	assert(s.add(1)==true);
	assert(s.add(10)==true);
	assert(s.add(7)==true);
	assert(s.add(1)==false);
	assert(s.add(10)==false);
	assert(s.add(-3)==true);
	assert(s.size() == 5);
	assert(s.search(10) == true);
	assert(s.search(16) == false);
	assert(s.remove(1) == true);
	assert(s.remove(6) == false);
	assert(s.size() == 4);

	
	SetIterator it = s.iterator();
	it.first();
	int sum = 0;
	while (it.valid()) {
		TElem e = it.getCurrent();
		sum += e;
		it.next();
	}
	assert(sum == 19);
	
	//testam inversarea
	Set s1;
	
	s1.add(1);
	s1.add(2);
	s1.add(3);
	s1.add(4); // ordinea ar fi 4 -> 3 -> 2 -> 1

	s1.reverse(); // dupa inversare 1 -> 2 -> 3 -> 4

	SetIterator it1 = s1.iterator();
	it1.first();
	assert(it1.getCurrent() == 1); // primul element este 1

	it1.next();
	assert(it1.getCurrent() == 2); // al doilea element este 2

	it1.next();
	assert(it1.getCurrent() == 3); // al treilea element este 3

	it1.next();
	assert(it1.getCurrent() == 4); // al patrulea element este 4

	it1.next();
	assert(!it1.valid()); //gata

	

}

