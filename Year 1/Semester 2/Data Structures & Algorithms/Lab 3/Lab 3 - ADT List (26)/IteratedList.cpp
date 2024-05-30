
#include <exception>
#include "ListIterator.h"
#include "IteratedList.h"

//BC=WC=TC= Theta(n) - n is the capacity of the list
IteratedList::IteratedList() : head(-1), tail(-1), firstFree(0), _size(0), capacity(10) {
	elements = new TElem[capacity];
	next = new int[capacity];
	prev = new int[capacity];

	for (int i = 0; i < capacity; i++) {
		next[i] = i + 1; 
		prev[i] = i - 1; 
	}
	next[capacity - 1] = -1;
	prev[0] = -1; 
}


//BC=WC=TC= Theta(1)
int IteratedList::size() const {
	return _size;
}


//BC=WC=TC= Theta(1)
bool IteratedList::isEmpty() const {
	return _size == 0;
}

//BC=WC=TC= Theta(1)
ListIterator IteratedList::first() const {
	if (_size > 0) {
		return ListIterator(*this, head, true);
	}
	return ListIterator(*this, -1, false);
}

//BC=WC=TC= Theta(1)
TElem IteratedList::getElement(ListIterator pos) const {
	if (!pos.valid()) {
		throw std::exception("Invalid iterator");
	}
	return elements[pos.getPosition()];
}

//BC=WC=TC= Theta(1)
TElem IteratedList::remove(ListIterator& pos) {
	if (!pos.valid()) {
		throw std::exception("Invalid iterator position");
	}

	int currentPos = pos.getPosition();
	TElem removedElement = elements[currentPos];

	if (prev[currentPos] != -1) {
		next[prev[currentPos]] = next[currentPos];
	}
	else {
		head = next[currentPos];
	}

	if (next[currentPos] != -1) {
		prev[next[currentPos]] = prev[currentPos];
	}
	else {
		tail = prev[currentPos];
	}

	next[currentPos] = firstFree;
	prev[currentPos] = -1; 
	firstFree = currentPos;

	_size--;

	if (currentPos == tail) {
		pos.setPosition(-1);
	}
	else {
		pos.next(); 
	}

	return removedElement;
}


//BC=WC=TC= Theta(n) - n is the capacity of the list
ListIterator IteratedList::search(TElem e) const {
	int current = head;
	while (current != -1) {
		if (elements[current] == e) {
			return ListIterator(*this, current, true);  
		}
		current = next[current];
	}
	return ListIterator(*this, -1, false); 
}



//BC=WC=TC= Theta(1)
TElem IteratedList::setElement(ListIterator pos, TElem e) {
	if (!pos.valid()) {
		throw std::exception("Invalid iterator position");
	}
	int currentPos = pos.getPosition();
	TElem oldElem = elements[currentPos];
	elements[currentPos] = e;
	return oldElem;
}


//BC=WC=TC= Theta(1)
void IteratedList::addToBeginning(TElem e) {
	int newPos = allocate();  
	elements[newPos] = e;
	prev[newPos] = -1; 
	next[newPos] = head;

	if (head != -1) {  
		prev[head] = newPos;
	}
	head = newPos;

	if (tail == -1) {  
		tail = newPos;
	}

	_size++;
}


void IteratedList::addToPosition(ListIterator& pos, TElem e) {
	if (!pos.valid()) {
		throw std::exception("Invalid iterator position");
	}

	int newPos = allocate();
	int currentPos = pos.getPosition();

	elements[newPos] = e;
	next[newPos] = next[currentPos];
	prev[newPos] = currentPos; 

	if (next[currentPos] != -1) { 
		prev[next[currentPos]] = newPos;
	}
	next[currentPos] = newPos; 

	if (tail == currentPos) { 
		tail = newPos; 
	}

	_size++;

	pos.setPosition(newPos);
}




//BC=WC=TC= Theta(1) 
void IteratedList::addToEnd(TElem e) {
	int newPos = allocate();  
	elements[newPos] = e;     
	next[newPos] = -1;        
	prev[newPos] = tail;      

	if (tail != -1) {         
		next[tail] = newPos;
	}
	tail = newPos;            

	if (head == -1) {         
		head = newPos;
	}

	_size++;                  
}

//BC=WC=TC= Theta(1)
int IteratedList::allocate() {
	if (firstFree == -1) { 
		resize();
	}
	int position = firstFree;
	firstFree = next[firstFree]; 
	return position;
}

//BC=WC=TC= Theta(n) - n is the capacity of the list
void IteratedList::resize() {
	int newCapacity = capacity * 2;  
	TElem* newElements = new TElem[newCapacity];
	int* newNext = new int[newCapacity];
	int* newPrev = new int[newCapacity];

	for (int i = 0; i < capacity; i++) {
		newElements[i] = elements[i];
		newNext[i] = next[i];
		newPrev[i] = prev[i];
	}

	for (int i = capacity; i < newCapacity - 1; i++) {
		newNext[i] = i + 1;  
		newPrev[i] = -1;    
	}
	newNext[newCapacity - 1] = -1;  

	if (firstFree == -1) {  
		firstFree = capacity;
	}

	delete[] elements;
	delete[] next;
	delete[] prev;

	elements = newElements;
	next = newNext;
	prev = newPrev;
	capacity = newCapacity;
}


//BC=WC=TC= Theta(1)
IteratedList::~IteratedList() {
	delete[] elements;
	delete[] next;
	delete[] prev;
}

//BC=Theta(1)
//WC=Theta(n)
//TC=O(n)
void IteratedList::removeBetween(ListIterator start, ListIterator end)
{
	if (!start.valid() || !end.valid()) 
		throw std::exception("Invalid iterator position");
	if (start.getPosition() > end.getPosition())
		throw std::exception("Invalid iterator position");

	int startPos = start.getPosition();
	int endPos = end.getPosition();

	int current = startPos;

	while (current != -1 and current != endPos) {
		int nextPos = next[current];
		if (prev[current] != -1) {
			next[prev[current]] = next[current];
		}
		else {
			head = next[current];
		}

		if (next[current] != -1) {
			prev[next[current]] = prev[current];
		}
		else {
			tail = prev[current];
		}

		next[current] = firstFree;
		prev[current] = -1;
		firstFree = current;

		current = nextPos;
		_size--;
	}
	start.setPosition(endPos);
}