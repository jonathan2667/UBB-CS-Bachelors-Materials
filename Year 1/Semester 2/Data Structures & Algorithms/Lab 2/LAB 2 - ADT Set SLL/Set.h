#pragma once
//DO NOT INCLUDE SETITERATOR

//DO NOT CHANGE THIS PART
#define NULL_TELEM -111111
typedef int TElem;
class SetIterator;

/*
Implement in C++ the given container (ADT) using a given representation and a linked list with 
dynamic allocation as a data structure. You are not allowed to use the list from STL or from any other 
library

 ADT Set – using a SLL.
*/

struct Node {
    TElem data;
    Node* next;
};

class Set {
	//DO NOT CHANGE THIS PART
	friend class SetIterator;

    private:
		Node* head;
        int length;


    public:
        //implicit constructor
        Set();

        //adds an element to the set
		//returns true if the element was added, false otherwise (if the element was already in the set and it was not added)
        bool add(TElem e);

        //removes an element from the set
		//returns true if e was removed, false otherwise
        bool remove(TElem e);

        //checks whether an element belongs to the set or not
        bool search(TElem elem) const;

        //returns the number of elements;
        int size() const;

        //check whether the set is empty or not;
        bool isEmpty() const;

        //return an iterator for the set
        SetIterator iterator() const;

        // destructor
        ~Set();


        //reverse pt lista inlantuita
        void reverse();
};





