#pragma once
#include "IteratedList.h"

//DO NOT CHANGE THIS PART
class IteratedList;
typedef int TElem;

class ListIterator{
	friend class IteratedList;
private:
	const IteratedList& list;   // Reference to the list being iterated.
	int current;                // Current position in the list.
	bool isValid;
	
public:
	ListIterator(const IteratedList& list, int current = -1, bool isValid = false);
	void first();
	void next();
	bool valid() const;
	TElem getCurrent() const;
	int getPosition() const;
	void setPosition(int position);
};


