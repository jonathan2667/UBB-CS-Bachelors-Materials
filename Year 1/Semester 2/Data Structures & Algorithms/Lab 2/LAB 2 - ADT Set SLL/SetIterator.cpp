#include "SetIterator.h"
#include "Set.h"
#include<stdexcept>

SetIterator::SetIterator(const Set& m) : set(m), currentNode(m.head) {
	// The iterator is initialized and points to the first element of the set, if any.
}

//BC = Theta(1) - constant
//WC = Theta(1) - constant
//TC =Theta(1)
void SetIterator::first() {
	currentNode = set.head;
}


//BC = Theta(1) - constant
//WC = Theta(1) - constant
//TC =Theta(1)
void SetIterator::next() {
	if (currentNode == nullptr) {
		throw std::exception("Iterator is not valid.");
	}
	currentNode = currentNode->next;
}

//BC = Theta(1) - constant
//WC = Theta(1) - constant
//TC =Theta(1)
TElem SetIterator::getCurrent() {
	if (currentNode == nullptr) {
		throw std::exception("Iterator is not valid.");
	}
	return currentNode->data;
}

//BC = Theta(1) - constant
//WC = Theta(1) - constant
//TC =Theta(1)
bool SetIterator::valid() const {
	return currentNode != nullptr;
}




