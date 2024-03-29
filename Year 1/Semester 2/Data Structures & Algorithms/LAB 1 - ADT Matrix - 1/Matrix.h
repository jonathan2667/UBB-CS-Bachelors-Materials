#pragma once

#include<iostream>
#include <utility>
using namespace std;
//DO NOT CHANGE THIS PART
typedef int TElem;
typedef std::pair<std::pair<int, int>, TElem> Triple;	
#define NULL_TELEM 0
#define NULL_TRIPLE {{-1,-1}, NULL_TELEM}

class MatrixIterator;

/*
LAB 1:

	ADT Matrix – represented as a sparse matrix, using a dynamic array of triples <line, column,
value> (value ≠ 0), ordered lexicographically considering the <line, column> of every
element.
*/


class Matrix {
	friend class MatrixIterator;

private:
	int nrL, nrC;
	Triple* triplets;
	int capacity, size; 
	void resize();

public:
	//constructor
	Matrix(int nrLines, int nrCols);

	//returns the number of lines
	int nrLines() const;

	//returns the number of columns
	int nrColumns() const;

	//returns the element from line i and column j (indexing starts from 0)
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem element(int i, int j) const;

	//modifies the value from line i and column j
	//returns the previous value from the position
	//throws exception if (i,j) is not a valid position in the Matrix
	TElem modify(int i, int j, TElem e);

	pair<int, int> findPositionOfElement(TElem e) const;
	
	MatrixIterator iterator() const;

	int numberOfNonZeroElems(int line) const;

	// destructor
	~Matrix();

};
