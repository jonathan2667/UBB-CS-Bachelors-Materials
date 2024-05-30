#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
#include <vector>
#include <exception>
#include <cmath>

using namespace std;

// BC = WC = TC = Theta(capacity)   
SortedMultiMap::SortedMultiMap(Relation r) : capacity(30), numElements(0), rel(r) {
	this->elements = new TElem[capacity];
	for (int i = 0; i < capacity; i++) {
		elements[i] = NULL_TELEM;
	}
}

// Best case = Theta(1) (when the element is added at the first try)
// Worst case = Theta(capacity) (when the element is added after a number of probes equal to the capacity)
// Average case = O(capacity) (when the element is added after a number of probes equal to the capacity)

void SortedMultiMap::add(TKey c, TValue v) {
	if (numElements >= capacity * 0.7) {
		resize();
	}

	int probe = 0;
	int idx = hash(c, probe);
	while (elements[idx] != NULL_TELEM) {
		probe++;
		idx = hash(c, probe);
	}

	elements[idx] = TElem(c, v);
	numElements++;

	//cout << "Added " << c << " " << v << " at " << idx << endl;
}





// Best case = Theta(1) (when the element is found at the first try)
// Worst case = Theta(capacity) (when the element is found after a number of probes equal to the capacity)
// Average case = O(capacity) (when the element is found after a number of probes equal to the capacity)
vector<TValue> SortedMultiMap::search(TKey c) const {
    vector<TValue> values;
	int probe = 0;
	int idx = hash(c, probe);
	while (elements[idx].first != c && elements[idx] != NULL_TELEM) {
		probe++;
		idx = hash(c, probe);
	}

	if (elements[idx].first == c) {
		values.push_back(elements[idx].second);
		probe++;
		idx = hash(c, probe);
		while (elements[idx].first == c) {
			values.push_back(elements[idx].second);
			probe++;
			idx = hash(c, probe);
		}
	}

	return values;
}


// Best case = Theta(1) (when the element is found at the first try)
// Worst case = Theta(capacity) (when the element is found after a number of probes equal to the capacity)
// Average case = O(capacity) (when the element is found after a number of probes equal to the capacity)
bool SortedMultiMap::remove(TKey c, TValue v) {
	//removes a key value pair from the sorted multimap
	//returns true if the pair was removed (it was part of the multimap), false if nothing is removed
	//when we remove a pair we do not remove all the pairs with the same key!!! very important
	//when we remove a pair we do not remove all the pairs with the same key!!! very
	
	int probe = 0;
	int idx = hash(c, probe);
	while (elements[idx].first != c && probe < capacity) {
		probe++;
		idx = hash(c, probe);
	}
	//cout << "Found " << c << " " << v << " at " << idx << endl;
	
	if (elements[idx].first == c && elements[idx].second == v) {
		elements[idx] = NULL_TELEM;
		numElements--;
		return true;
	}

	return false;
	

}


//BC= WC = AC = Theta(1)
//returns the number of key-value pairs from the sorted multimap
int SortedMultiMap::size() const {
		return numElements;
}

//BC= WC = AC = Theta(1)
//verifies if the sorted multi map is empty
bool SortedMultiMap::isEmpty() const {
	return numElements == 0;
}

//BC= WC = AC = Theta(1)
SMMIterator SortedMultiMap::iterator() const {
	return SMMIterator(*this);
}

//BC= WC = AC = Theta(1)
SortedMultiMap::~SortedMultiMap() {
	delete[] elements;
}

//BC= WC = AC = Theta(1) - calculations are done in constant time
int SortedMultiMap::hash(TKey key, int probe) const {
    int hashValue = abs(key);
    return (hashValue + probe * probe) % capacity;
}

//Best case = Theta(1) (when n <= 3)
//Worst case = Theta(sqrt(n)) (when n is a prime number)
//Average case = O(sqrt(n)) (when n is a prime number)
bool SortedMultiMap::isPrime(int n) {
    if (n <= 1)
        return false;
    if (n <= 3)
        return true;
    if (n % 2 == 0 || n % 3 == 0)
        return false;
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    }

    return true;
}

//Best case = Theta(1) if number is already orime
//Worst case = Theta(sqrt(n)) (maximal time to find the enxt prime)
//Average case = O(sqrt(n)) 
int SortedMultiMap::findNextPrime(int num) {
    if (num <= 1)
        return 2;
    int nextPrime = num;
    if (nextPrime % 2 == 0)
        nextPrime++;
    while (!isPrime(nextPrime)) {
        nextPrime += 2;
    }

    return nextPrime;
}

//BC= WC = AC = Theta(capacity^2) - we need to copy all the elements and rehash them
void SortedMultiMap::resize() {
    int newCapacity = findNextPrime(capacity * 2);
	TElem* newElements = new TElem[newCapacity];
	for (int i = 0; i < newCapacity; i++) {
		newElements[i] = NULL_TELEM;
	}

	for (int i = 0; i < capacity; i++) {
		if (elements[i] != NULL_TELEM) {
			int probe = 0;
			int idx = hash(elements[i].first, probe);
			while (newElements[idx] != NULL_TELEM) {
				probe++;
				idx = hash(elements[i].first, probe);
			}
			newElements[idx] = elements[i];
		}
	}

	delete[] elements;
	elements = newElements;
	capacity = newCapacity;

}


