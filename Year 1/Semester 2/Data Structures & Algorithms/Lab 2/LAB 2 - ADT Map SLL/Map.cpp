#include "Map.h"
#include "MapIterator.h"
// Complexity: Theta(1)
Map::Map() : head(nullptr), length(0) {
	//TODO - Implementation
}


// Complexity: Theta(n), where n is the number of elements in the map.
Map::~Map() {
	Node* current = head;
	while (current != nullptr) {
		Node* next = current->next;
		delete current;
		current = next;
	}
}

// BC: Theta(1) - if the key is the first element 
// WC: Theta(n) - if the key does not exist 
// TC: O(n)
TValue Map::add(TKey key, TValue value){
	Node* current = head;
	Node* previous = nullptr;
	while (current != nullptr) {
		if (current->elem.first == key) {
			TValue old = current->elem.second;
			current->elem.second = value;
			return old;
		}
		previous = current;
		current = current->next;
	}
	TElem new_elem = std::make_pair(key, value);
	Node* new_node = new Node(new_elem, head);
	head = new_node;
	length++;
	return NULL_TVALUE;
}

// BC: Theta(1) - if the key is at the head of the list.
// WC: Theta(n) - if the key is not in the list.
// TC: O(n)
TValue Map::search(TKey key) const{
	Node* current = head;
	while (current != nullptr) {
		if (current->elem.first == key) {
			return current->elem.second;
		}
		current = current->next;
	}
	return NULL_TVALUE;
}

// BC: Theta(1) - if the key is at the head of the list.
// WC: Theta(n) - if the key is not in the list.
// TC: O(n)
TValue Map::remove(TKey key){
	Node* current = head;
	Node* previous = nullptr;
	while (current != nullptr) {
		if (current->elem.first == key) {
			TValue removed_value = current->elem.second;
			if (previous == nullptr) {
				head = current->next; // removing the first node
			}
			else {
				previous->next = current->next;
			}
			delete current;
			length--;
			return removed_value;
		}
		previous = current;
		current = current->next;
	}
	return NULL_TVALUE;
}

// Returns the number of key-value pairs in the map.
// Complexity: Theta(1)
int Map::size() const {
	return length;
}

// Checks if the map is empty.
// Complexity: Theta(1)
bool Map::isEmpty() const{
	return head == nullptr;
}

// Returns an iterator for the map.
// Complexity: Theta(1)
MapIterator Map::iterator() const {
	return MapIterator(*this);
}



//keeps in the map only those pairs whose key respects the given condition
// Theta(n)
void Map::filter(Condition cond) {
	Node* current = head;
	Node* previous = nullptr;
	while (current != nullptr) {
		if (!cond(current->elem.first)) {
			Node* next = current->next;
			if (previous == nullptr) {
				head = next;
			}
			else {
				previous->next = next;
			}
			delete current;
			current = next;
			length--;
		}
		else {
			previous = current;
			current = current->next;
		}
	}
}