#include "FixedCapBiMap.h"
#include "FixedCapBiMapIterator.h"
#include <exception>
using namespace std;


FixedCapBiMapIterator::FixedCapBiMapIterator(const FixedCapBiMap& d) : map(d) {
	this->currentPosition = 0;
}


void FixedCapBiMapIterator::first() {
	this->currentPosition = 0;
}


void FixedCapBiMapIterator::next() {
	if (this->currentPosition == this->map.mapSize)
		throw exception();
	this->currentPosition++;
}


TElem FixedCapBiMapIterator::getCurrent(){
	if (this->currentPosition == this->map.mapSize)
		throw exception();
	return this->map.elements[this->currentPosition];
}


bool FixedCapBiMapIterator::valid() const {
	return this->currentPosition < this->map.mapSize;
}



