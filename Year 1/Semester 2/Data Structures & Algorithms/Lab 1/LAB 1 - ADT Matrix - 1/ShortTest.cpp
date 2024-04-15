#include <assert.h>
#include "Matrix.h"
#include "MatrixIterator.h"

using namespace std;

void testAll() { 
    // Existing setup and tests
    Matrix m(4, 4);
    assert(m.nrLines() == 4);
    assert(m.nrColumns() == 4);
    m.modify(1, 1, 5);
    assert(m.element(1, 1) == 5);
    m.modify(1, 1, 6);
    assert(m.element(1, 2) == NULL_TELEM);


    pair<int, int> position = m.findPositionOfElement(6);
    assert(position.first == 1 && position.second == 1); 

    position = m.findPositionOfElement(5);
    assert(position.first == -1 && position.second == -1);

    position = m.findPositionOfElement(999);
    assert(position.first == -1 && position.second == -1); 

    MatrixIterator it = m.iterator();
    assert(it.valid()); // The iterator should be valid at the start.

    // Check the first element
    TElem firstElem = it.getCurrent();
    assert(firstElem == 6); // The first non-NULL_TELEM should be 6 based on previous modifications.

    it.next(); // Move to the next element.
    assert(!it.valid()); // There should be no more elements, so iterator should now be invalid.

    // Reinitializing iterator for a full pass
    MatrixIterator it2 = m.iterator();
    int nonZeroCount = 0;
    while (it2.valid()) {
        TElem elem = it2.getCurrent();
        assert(elem != NULL_TELEM); // Ensure the element is indeed non-zero.
        nonZeroCount++;
        it2.next(); // Move to the next element.
    }

    assert(nonZeroCount == 1); 



    /* NON ZERO ELEMS*/
    
    Matrix mm(4, 4);
    for (int line = 0; line < mm.nrLines(); ++line) {
        assert(mm.numberOfNonZeroElems(line) == 0);
    }

    mm.modify(1, 1, 5); 
    assert(mm.numberOfNonZeroElems(1) == 1);

    mm.modify(1, 2, 3);
    assert(mm.numberOfNonZeroElems(1) == 2);

    assert(mm.numberOfNonZeroElems(2) == 0); 

    bool exceptionThrown = false;
    try {
        mm.numberOfNonZeroElems(-1); 
    }
    catch (const std::out_of_range&) {
        exceptionThrown = true;
    }
    assert(exceptionThrown);

    exceptionThrown = false;
    try {
        mm.numberOfNonZeroElems(mm.nrLines()); 
    }
    catch (const std::out_of_range&) {
        exceptionThrown = true;
    }
    assert(exceptionThrown);
    
}