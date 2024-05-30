#pragma once

#include "SortedMultiMap.h"


class SMMIterator{
	friend class SortedMultiMap;
private:
	//DO NOT CHANGE THIS PART
	const SortedMultiMap& map;
	SMMIterator(const SortedMultiMap& map);

	//TODO - Representation
	TElem* sortedElements;  // sorted elements
	int current;            // pozitia
	int totalElements;      

	void sortElements();    
	
public:
	~SMMIterator();
	void first();
	void next();
	bool valid() const;
   	TElem getCurrent() const;
	
};

