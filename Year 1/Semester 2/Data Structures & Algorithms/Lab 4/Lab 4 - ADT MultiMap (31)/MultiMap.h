#pragma once
#include<vector>
#include<utility>
//DO NOT INCLUDE MultiMapIterator

	/*
	31. ADT MultiMap – using a hashtable with separate chaining in which unique keys are stored
	with a dynamic array of the associated values
	*/

using namespace std;

//DO NOT CHANGE THIS PART
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TELEM pair<int,int>(-111111, -111111)
class MultiMapIterator;

class MultiMap
{
	friend class MultiMapIterator;

private:
	//TODO - Representation

	struct Node {
		TKey key;
		TValue* values;
		int valuesCount;
		int valuesCapacity;
		Node* next;

		Node(TKey k) : key(k), values(new TValue[4]), valuesCount(0), valuesCapacity(4), next(nullptr) {}

		~Node() {
			delete[] values;
		}

		void addValue(TValue value) {
			if (valuesCount == valuesCapacity) {
				valuesCapacity *= 2;
				TValue* newValues = new TValue[valuesCapacity];
				for (int i = 0; i < valuesCount; i++) {
					newValues[i] = values[i];
				}
				delete[] values;
				values = newValues;
			}
			values[valuesCount++] = value;
		}
	};

	Node** table;
	int capacity;
	int numberOfElements;

	int hash(TKey key) const {
		return abs(key) % capacity;
	}

	void rehash() {
		int oldCapacity = capacity;
		capacity *= 2;
		Node** newTable = new Node * [capacity] {};

		for (int i = 0; i < oldCapacity; i++) {
			Node* entry = table[i];
			while (entry != nullptr) {
				Node* next = entry->next;
				int index = hash(entry->key);
				entry->next = newTable[index];
				newTable[index] = entry;
				entry = next;
			}
		}

		delete[] table;
		table = newTable;
	}

public:
	//constructor
	MultiMap();

	//adds a key value pair to the multimap
	void add(TKey c, TValue v);

	//removes a key value pair from the multimap
	//returns true if the pair was removed (if it was in the multimap) and false otherwise
	bool remove(TKey c, TValue v);

	//returns the vector of values associated to a key. If the key is not in the MultiMap, the vector is empty
	vector<TValue> search(TKey c) const;

	//returns the number of pairs from the multimap
	int size() const;

	//checks whether the multimap is empty
	bool isEmpty() const;

	//returns an iterator for the multimap
	MultiMapIterator iterator() const;

	//descturctor
	~MultiMap();

	//adds all pairs from m, whose key is not in the multimap already
	//returns the number of pairs added
	int addIfNotPresent(MultiMap& a);
};


