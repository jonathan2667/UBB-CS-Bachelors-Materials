#pragma once
#include <utility>
#include <exception>

using namespace std;

//DO NOT INCLUDE MAPITERATOR


//DO NOT CHANGE THIS PART
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
typedef std::pair<TValue, TValue>  ValuePair;
#define NULL_TVALUE -111111
#define NULL_TELEM pair<TKey, TValue>(-111111, -111111)
class FixedCapBiMapIterator;


//This is the interface of a Fixed Capacity Bi-Map container
//Bi-Map means that it contains key-value pairs. One key can have at most two associated values (so there can be at most two pairs with the same key. 
//It can happen that we have exactly the same key-value pair twice). 
//Fixed capacity means that the container has a fixed capacity, provided when it is created. Once the total number of elements is equal to that fixed capacity, no other elements can be added.
class FixedCapBiMap {

	//DO NOT CHANGE THIS PART
	friend class FixedCapBiMapIterator;

	private:
		TElem * elements;
		int capacity;
		int mapSize;

	public:

	//constructor of the container. Creates a FixedCapBiMap with the given capacity. 
	//If capacity is zero or negative an exception is thrown
	FixedCapBiMap(int capacity);

	// adds a pair (key,value) to the FixedCapBiMap
	//if the FixedCapBiMap is full (the number of elements is equal to the capacity provided at creation),  an exception is thrown.
	//if the key already has two associated values in the FixedCapBiMap, the new pair is not added and the operation returns false.
	//if the key does not exist or if it has only one associated value, the new pair is added and true is returned
	bool add(TKey c, TValue v);

	//searches for a key in the FixedCapBiMap.
	//It returns a pair of values. 
	//If c is not in the FixedCapBiMap, both elements of the pair have the value NULL_TVALUE.
	//If c is in the FixedCapBiMap once, the first component of the pair is its value, the second component is NULL_TVALUE.
	//If c is in the FixedCapBiMap twice, the returned pair contains the two values associated to it (in any order)
	ValuePair search(TKey c) const;

	//removes a key - value pair from the FixedCapBiMap 
	//if the pair was removed, the operation returns true, otherwise (if the given pair was not in the FixedCapBiMap) it returns false
	bool remove(TKey c, TValue v);

	//returns the number of pairs (key,value) from the FixedCapBiMap
	int size() const;

	//checks whether the FixedCapBiMap is empty or not
	bool isEmpty() const;

	//checks whether the FixedCapBiMap is full or not
	bool isFull() const;

	//returns an iterator for the FixedCapBiMap
	FixedCapBiMapIterator iterator() const;

	// destructor
	~FixedCapBiMap();

};



