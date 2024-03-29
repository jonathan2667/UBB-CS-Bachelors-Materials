#include "MatrixIterator.h"

MatrixIterator::MatrixIterator(const Matrix& matrix) : matrix(matrix), currentPosition(0) {
    // Advance to the first non-NULL_TELEM element, if necessary
    while (currentPosition < matrix.size && matrix.triplets[currentPosition].second == NULL_TELEM) {
        ++currentPosition;
    }
}

bool MatrixIterator::valid() const {
    return currentPosition < matrix.size;
}

TElem MatrixIterator::getCurrent() {
    if (!valid()) {
        throw std::out_of_range("Iterator out of range.");
    }
    return matrix.triplets[currentPosition].second;
}

void MatrixIterator::next() {
    do {
        ++currentPosition;
    } while (currentPosition < matrix.size && matrix.triplets[currentPosition].second == NULL_TELEM);
}


