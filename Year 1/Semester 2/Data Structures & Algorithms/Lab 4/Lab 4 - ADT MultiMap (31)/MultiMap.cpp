#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

using namespace std;


//constructor
//BC=WC=TC=Theta(capacity)
MultiMap::MultiMap() : capacity(10), numberOfElements(0) {
	table = new Node * [capacity] {};
}


//adds a key value pair to the multimap
//BC=Theta(1), WC=Theta(capacity), TC=O(capacity)
void MultiMap::add(TKey key, TValue value) {
	
	int index = hash(key);
	Node* entry = table[index];
	while (entry != nullptr && entry->key != key) {
		entry = entry->next;
	}
	if (entry == nullptr) {
		entry = new Node(key);
		entry->next = table[index];
		table[index] = entry;
	}
	entry->addValue(value);
	numberOfElements++;
	if (numberOfElements / capacity > 1) { 
		rehash();
	}
}

//removes a key value pair from the multimap
//returns true if the pair was removed (if it was in the multimap) and false otherwise
//BC=Theta(1), WC=Theta(capacity), TC=O(capacity)
bool MultiMap::remove(TKey key, TValue value) {
	int index = hash(key);
	Node* entry = table[index];
	Node* prev = nullptr;

	while (entry != nullptr) {
		if (entry->key == key) {
			for (int i = 0; i < entry->valuesCount; ++i) {
				if (entry->values[i] == value) {
					for (int j = i; j < entry->valuesCount - 1; ++j) {
						entry->values[j] = entry->values[j + 1];
					}
					entry->valuesCount--;
					numberOfElements--;

					if (entry->valuesCount == 0) {
						if (prev == nullptr) { //removing the head
							table[index] = entry->next;
						}
						else {
							prev->next = entry->next;
						}
						delete entry;
					}
					return true;
				}
			}
		}
		prev = entry;
		entry = entry->next;
	}
	return false;

}

//returns a vector with all the values to which the key is mapped
//BC=Theta(1), WC=Theta(capacity), TC=O(capacity)
vector<TValue> MultiMap::search(TKey key) const {
	int index = hash(key);
	Node* entry = table[index];
	while (entry != nullptr) {
		if (entry->key == key) {
			vector<TValue> values(entry->values, entry->values + entry->valuesCount);
			return values;
		}
		entry = entry->next;
	}
	return vector<TValue>(); 
}

//BC=Theta(1), WC=Theta(1), TC=Theta(1)
int MultiMap::size() const {
	return numberOfElements;
}

//BC=Theta(1), WC=Theta(1), TC=Theta(1)
bool MultiMap::isEmpty() const {
	return numberOfElements == 0;
}

//BC=Theta(1), WC=Theta(1), TC=Theta(1)
MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}

//BC=WC=TC=Theta(capacity)
MultiMap::~MultiMap() {
	//TODO - Implementation
	for (int i = 0; i < capacity; i++) {
		Node* current = table[i];
		while (current != nullptr) {
			Node* next = current->next;
			delete current;
			current = next;
		}
	}
	delete[] table;

}

//adds all pairs from m, whose key is not in the multimap already
//returns the number of pairs added
//BC= Theta(m.capacity * nod.capacity)
//WC= Theta(m.capacity * (m.size + nod.capacity))
// TC=O(m.capacity * m.size * nod.capacity)
int MultiMap::addIfNotPresent(MultiMap& m) {
	int count = 0;
	for (int i = 0; i < m.capacity; i++) {
		Node* current = m.table[i];
		while (current != nullptr) {
			vector<TValue> values = this->search(current->key);
			if (values.empty()) { 
				for (int j = 0; j < current->valuesCount; j++) {
					this->add(current->key, current->values[j]);
					count++;
				}
			}
			current = current->next;
		}
	}
	return count;
}
