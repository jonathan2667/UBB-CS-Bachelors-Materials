#Example for Extra Reading 2.

#Below you find the implementation for a Bag with frequencies and with Python-style iterator, where 
#the iterator is not a separate class)
class BagWithFrequencyPI1:
    def __init__(self):
        self.__elems = [] #List with unique elements
        self.__frequencies = [] # list with frequencies

    def add(self, elem):
        #check if elem is already in the bag. If it is, increase frequency, otherwise add new element  with frequency 1
        found = False
        index = 0
        while index < len(self.__elems) and not found:
            if self.__elems[index] == elem:
                self.__frequencies[index] += 1
                found = True
            index = index + 1
        if not found:
            self.__elems.append(elem)
            self.__frequencies.append(1)

    #remove returns True if elem was removed and False otherwise
    def remove(self, elem):
        #we look for the position where the element is, and if we find it, we decrement frequency (if it is greater than 1) or remove the element and its frequency (if the frequency would become 0)
        index = 0
        while index < len(self.__elems):
            if self.__elems[index] == elem:
                if self.__frequencies[index] > 1:
                    self.__frequencies[index] -= 1
                else:
                    del self.__elems[index]
                    del self.__frequencies[index]
                return True
            index = index + 1
        return False

    def search(self, elem):
        return elem in self.__elems

    def size(self):
        #number of elements is the sum of frequencies
        count = 0
        for e in self.__frequencies:
            count = count + e
        return count

    def nrOccurrences(self, elem):
        found = False
        index = 0
        count = 0
        while index < len(self.__elems) and not found:
            if self.__elems[index] == elem:
                count = self.__frequencies[index]
                found = True
            index = index + 1
        return count

    def __iter__(self):
        #operation to create an iterator
        self.__currentPos = 0
        self.__currentFr = 1
        return self

    def __next__(self):
        #operation from the iterator protocol
        if self.__currentPos == len(self.__elems):
            raise StopIteration
        currentElem = self.__elems[self.__currentPos]
        if self.__currentFr < self.__frequencies[self.__currentPos]:
            self.__currentFr += 1
        else:
            self.__currentPos += 1
            self.__currentFr = 1
        return currentElem
    
#----------------------------------Tests and examples-------------------    
def createBag():
    b = BagWithFrequencyPI1()
    for i in range(10):
        b.add(i)
        b.add(i * 2)
    return b

def test1():
    #create a bag, add some elements:
    b = createBag()
    
    #print the content with an iterator:
    print('Printing elements')    
    for elem in b:
        print(elem)
        
    #print pairs of elements
    print('Printing pairs of elements')
    for elem1 in b:
        for elem2 in b:
            print(elem1, ' ', elem2)
    
    #print triples of elements
    print('Printing triples of elements')
    for elem1 in b:
        for elem2 in b:
            for elem3 in b:
                print(elem1, ' ', elem2, ' ', elem3)


def test2():
    b = createBag()
    iterator = b.__iter__()
    
    #btw iterator and b are the same object
    print(b is iterator)
    
    stop = False
    while not stop:
        try:
            elem = iterator.__next__()
        except StopIteration:
            stop = True
        else:
            print(elem)


def test2B():
    #same as test2, but we are going to use the fact that b and iterator are the same and not have an iterator variable
    #works just as well, but it might look strange to do next on the container.
    b = createBag()
    b.__iter__()
    
    stop = False
    while not stop:
        try:
            elem = b.__next__()
        except StopIteration:
            stop = True
        else:
            print(elem)


def test3():
    b = createBag()
    iterator = iter(b)
    stop = False
    while not stop:
        try:
            elem = next(iterator)
        except StopIteration:
            stop = True
        else:
            print(elem)


test1()
test2()             
test2B()
test3()            