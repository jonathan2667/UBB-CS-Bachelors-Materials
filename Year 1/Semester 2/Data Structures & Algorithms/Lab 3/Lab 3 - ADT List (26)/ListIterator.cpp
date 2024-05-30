#include "ListIterator.h"
#include "IteratedList.h"
#include <exception>


ListIterator::ListIterator(const IteratedList& list, int current, bool isValid)
    : list(list), current(current), isValid(isValid) {}


void ListIterator::first() {
    current = list.head;
    isValid = (current != -1);
}

void ListIterator::next() {
    if (current == -1 || !isValid) {
        throw std::exception("Iterator cannot move next from an invalid position");
    }
    current = list.next[current];
}

// Checks if the current position is valid
bool ListIterator::valid() const {
    return current != -1 && isValid;
}

TElem ListIterator::getCurrent() const {
    if (!isValid) {
        throw std::exception("Invalid iterator position");
    }
    if (valid()) {
        return list.elements[current];
    }
    throw std::exception("Invalid iterator position");
}

int ListIterator::getPosition() const {
    return current;
}

void ListIterator::setPosition(int position) {
    if (position < 0 || position >= list._size) {
        throw std::exception("Invalid position");
    }
    current = position;
}

