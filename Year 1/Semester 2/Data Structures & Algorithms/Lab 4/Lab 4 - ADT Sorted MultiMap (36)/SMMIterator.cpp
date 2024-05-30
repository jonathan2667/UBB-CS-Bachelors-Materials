#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <stdexcept> 


// BC = WC = AC = Theta(n^2) becasue of the bubble sort
SMMIterator::SMMIterator(const SortedMultiMap& map) : map(map), current(0), totalElements(0) {
       //In the constructor of the iterator create a sorted array of pairs and use it for iterating.
    totalElements = map.size();
    sortedElements = new TElem[totalElements];
    int index = 0;

    for (int i = 0; i < map.capacity; i++) {
        if (map.elements[i] != NULL_TELEM) {
            sortedElements[index++] = map.elements[i];
        }
    }

    sortElements();
}

// BC = WC = AC = Theta(1)
SMMIterator::~SMMIterator() {
    delete[] sortedElements;  
}

// BC = WC = AC = Theta(1)
void SMMIterator::first() {
    current = 0; 
}

// BC = WC = AC = Theta(1)
void SMMIterator::next() {
    if (!valid()) {
        throw std::out_of_range("Iterator out of bounds.");
    }
    current++;
}

// BC = WC = AC = Theta(1)
bool SMMIterator::valid() const {
    return current < totalElements;
}

// BC = WC = AC = Theta(1)
TElem SMMIterator::getCurrent() const {
    if (!valid()) {
        throw std::out_of_range("Invalid iterator access.");
    }
    return sortedElements[current];
}

// Bubble sort the elements based on the relation
// BC = Theta(n)
// WC = AC = Theta(n^2)
void SMMIterator::sortElements() {
    
    for (int i = 0; i < totalElements - 1; i++) {
        for (int j = 0; j < totalElements - i - 1; j++) {
            if (!map.rel(sortedElements[j].first, sortedElements[j + 1].first)) {
                TElem temp = sortedElements[j];
                sortedElements[j] = sortedElements[j + 1];
                sortedElements[j + 1] = temp;
            }
        }
    }
}
