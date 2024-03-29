#include "Matrix.h" 
#include "MatrixIterator.h"
#include <exception> 

using namespace std;

// Constructor: Initializes a new Matrix object with specified dimensions.
// Time complexity:
// - Best case: Theta(1) - Constant time operation regardless of input size.
// - Worst case: Theta(1) - Same as best case, operations do not depend on input size.
// - Average case: Theta(1) - Consistent execution time, not input-dependent.
Matrix::Matrix(int nrLines, int nrCols) {
    this->nrL = nrLines; 
    this->nrC = nrCols; 
    this->size = 0; 
    this->capacity = 1; 
    this->triplets = new Triple[capacity]; 
}

// Returns the number of rows in the matrix.
// Time complexity:
// - Best case: Theta(1) - Direct access to a member variable.
// - Worst case: Theta(1) - Same as best case.
// - Average case: Theta(1) - Consistent execution time.
int Matrix::nrLines() const {
    return this->nrL; // Return the stored number of lines (rows).
}

// Returns the number of columns in the matrix.
// Time complexity:
// - Best case: Theta(1) - Direct access to a member variable.
// - Worst case: Theta(1) - Same as best case.
// - Average case: Theta(1) - Consistent execution time
int Matrix::nrColumns() const {
    return this->nrC; // Return the stored number of columns.
}

// Retrieves the element at a specific position, throws if out of bounds.
// Time complexity:
// - Best case: Theta(1) - The first element checked is the target.
// - Worst case: Theta(n) - The element is either not found or is the last one checked.
// - Average case: O(n) - Assumes elements are evenly distributed over possible positions.
TElem Matrix::element(int i, int j) const {
    if (i < 0 || i >= this->nrL || j < 0 || j >= this->nrC) {
        throw out_of_range("Position is out of range.");
    }
    for (int k = 0; k < this->size; ++k) {
        if (this->triplets[k].first.first == i && this->triplets[k].first.second == j) {
            return this->triplets[k].second; 
        }
    }
    return NULL_TELEM; 
}

// Doubles the capacity of the storage array when more space is needed.
// Time complexity:
// - Best case: Theta(n) - Directly proportional to the current size due to the need to copy elements.
// - Worst case: Theta(n) - Same as best case, involves copying existing elements to a new array.
// - Average case: Theta(n) - Copying of elements is always required, making it linear time complexity.
void Matrix::resize() {
    this->capacity *= 2;
    Triple* newTriplets = new Triple[capacity];
    for (int i = 0; i < size; ++i) {
        newTriplets[i] = this->triplets[i];
    }
    delete[] this->triplets;
    this->triplets = newTriplets;
}

// Modifies or inserts an element at a specified position.
// Time complexity:
// - Best case: Theta(1) - The element to modify or remove is found immediately.
// - Worst case: Theta(n) - The element is either added as a new element or is the last one checked before modification/removal.
// - Average case: O(n) - Assumes a uniform distribution of element positions.
TElem Matrix::modify(int i, int j, TElem e) {
    if (i < 0 || i >= this->nrL || j < 0 || j >= this->nrC) {
        throw out_of_range("Position is out of range.");
    }

    int pos = 0;
    while (pos < size && (triplets[pos].first.first < i || (triplets[pos].first.first == i && triplets[pos].first.second < j))) {
        pos++;
    }

    if (pos < size && triplets[pos].first.first == i && triplets[pos].first.second == j) {
        TElem old = triplets[pos].second;
        if (e == NULL_TELEM) {
            for (int k = pos; k < size - 1; k++) {
                triplets[k] = triplets[k + 1];
            }
            size--; 
        }
        else {
            triplets[pos].second = e;
        }
    }
    else if (e != NULL_TELEM) {
        if (this->size == this->capacity) {
            resize();
        }
        // Shift elements to the right to make space
        for (int k = size; k > pos; k--) {
            triplets[k] = triplets[k - 1];
        }
        triplets[pos] = { {i, j}, e };
        size++;
        return NULL_TELEM;
    }

    return NULL_TELEM;
}


// Best case: Theta(1) - The element is found at the first position.
// Worst case: Theta(n) - The element is found at the last position or not found.
// Average case: O(n) - The element is found in the middle or not found.
pair<int, int> Matrix::findPositionOfElement(TElem e) const {
    for (int k = 0; k < this->size; ++k) { // Loop through the stored elements.
        if (this->triplets[k].second == e) { // If the current element matches the search target,
            return { this->triplets[k].first.first, this->triplets[k].first.second }; // Return its position.
        }
    }
   return { -1, -1 }; // Return an invalid position if the element is not found.
}

// Destructor: Cleans up dynamically allocated memory.
// Time complexity:
// - Best case: Theta(1) - Deletion of the array is a constant time operation.
// - Worst case: Theta(1) - Same as best case, does not depend on the size of the array.
// - Average case: Theta(1) - Consistent execution time.
Matrix::~Matrix() {
    delete[] this->triplets; // Free the memory allocated for the triplets array.
}

// Time complexity:
// - Best case: Theta(1) - line exception is thrown immediately.
// - Worst case: Theta(n) - The line is valid and all elements are checked.
// Total time complexity: O(n)
int Matrix::numberOfNonZeroElems(int line) const {
    if (line < 0 || line >= nrL) {
        throw out_of_range("Line index is out of range.");
    }

    int count = 0;
    for (int i = 0; i < size; ++i) {
        if (triplets[i].first.first == line && triplets[i].second != NULL_TELEM) {
            ++count;
        }
    }

    return count;
}

MatrixIterator Matrix::iterator() const {
    return MatrixIterator(*this);
}
