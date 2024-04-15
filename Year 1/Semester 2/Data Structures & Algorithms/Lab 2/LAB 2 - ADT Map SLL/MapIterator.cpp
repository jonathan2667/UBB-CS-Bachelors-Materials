#include "Map.h"
#include "MapIterator.h"
#include <exception>
using namespace std;


// Complexity: Theta(1) 
MapIterator::MapIterator(const Map& d) : map(d), current(d.head)
{
	//TODO - Implementation
}


// Complexity: Theta(1) 
void MapIterator::first() {
	current = map.head;
}

// Complexity: Theta(1) 
void MapIterator::next() {
	if (!current) {
		throw std::exception("Iterator not valid");
	}
	current = current->next;
}


// Complexity: Theta(1) 
TElem MapIterator::getCurrent(){
	if (!current) {
		throw std::exception("Iterator not valid");
	}
	return current->elem;
}


// Complexity: Theta(1) 
bool MapIterator::valid() const {
	return current != nullptr;
}



