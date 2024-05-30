#include "MultiMapIterator.h"
#include "MultiMap.h"
#include <stdexcept>

//BC=WC=AC=Theta(1)
MultiMapIterator::MultiMapIterator(const MultiMap& c) : col(c), currentTableIndex(0), currentNode(nullptr), currentValueIndex(0) {
	first();  
}

//BC=WC=TC=Theta(capacity)
TElem MultiMapIterator::getCurrent() const {
    if (!valid())
        throw std::out_of_range("Iterator is not valid.");
    return std::make_pair(currentNode->key, currentNode->values[currentValueIndex]);
}

//BC=WC=AC=Theta(1)
bool MultiMapIterator::valid() const {
    return currentNode != nullptr;
}

//BC=WC=AC=Theta(1)
void MultiMapIterator::next() {
    if (!valid())
        throw std::exception();  

    if (currentValueIndex < currentNode->valuesCount - 1) {
        currentValueIndex++;
    }
    else {
        currentValueIndex = 0;  
        currentNode = currentNode->next;
        if (!currentNode) {  // no next node in the list, move to the next bucket
            currentTableIndex++;
            while (currentTableIndex < col.capacity && !col.table[currentTableIndex]) {
                currentTableIndex++;
            }
            if (currentTableIndex < col.capacity) {
                currentNode = col.table[currentTableIndex];
            }
            else {
                currentNode = nullptr;  //
            }
        }
    }
}

//BC=WC=AC=Theta(1)
void MultiMapIterator::first() {
	currentTableIndex = 0;
	while (currentTableIndex < col.capacity && !col.table[currentTableIndex]) {
		currentTableIndex++;
	}

	if (currentTableIndex < col.capacity) {
		currentNode = col.table[currentTableIndex];
		currentValueIndex = 0;
	}
	else {
		currentNode = nullptr;  
	}
}
