#pragma once
#include <utility>
//DO NOT INCLUDE MAPITERATOR

/*
11. ADT Map – using a SLL with (key, value) pairs
Implement in C++ the given container (ADT) using a given representation and a linked list with
dynamic allocation as a data structure. You are not allowed to use the list from STL or from any other
library.
*/


//DO NOT CHANGE THIS PART
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TELEM pair<TKey, TValue>(-111111, -111111)
typedef bool(*Condition)(TKey);
class MapIterator;

struct Node {
	TElem elem;
	Node* next;

	Node(TElem e, Node* n = nullptr) : elem(e), next(n) {}
};


class Map {
	//DO NOT CHANGE THIS PART
	friend class MapIterator;

	private:
		//TODO - Representation
		Node* head;
		int length;

	public:

	// implicit constructor
	Map();

	// adds a pair (key,value) to the map
	//if the key already exists in the map, then the value associated to the key is replaced by the new value and the old value is returned
	//if the key does not exist, a new pair is added and the value null is returned
	TValue add(TKey c, TValue v);

	//searches for the key and returns the value associated with the key if the map contains the key or null: NULL_TVALUE otherwise
	TValue search(TKey c) const;

	//removes a key from the map and returns the value associated with the key if the key existed ot null: NULL_TVALUE otherwise
	TValue remove(TKey c);

	//returns the number of pairs (key,value) from the map
	int size() const;

	//checks whether the map is empty or not
	bool isEmpty() const;

	//returns an iterator for the map
	MapIterator iterator() const;

	// destructor
	~Map();

	void filter(Condition cond);

};



