#pragma once

#include "Matrix.h" 
#include <stdexcept>

class MatrixIterator {
private:
    const Matrix& matrix;
    int currentPosition;

public:
    MatrixIterator(const Matrix& matrix);

    bool valid() const;
    TElem getCurrent();
    void next();
};

