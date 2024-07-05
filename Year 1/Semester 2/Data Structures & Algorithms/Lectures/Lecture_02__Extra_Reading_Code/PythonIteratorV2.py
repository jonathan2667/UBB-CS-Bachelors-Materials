#Example for Extra Reading 2

#Below you have the implementation of a Bag with frequencies and with Python-style 
#iterator (iterator is a separate class)
class BagWithFrequencyPI2:
    def __init__(self):
        self.__elems = [] #unique elements
        self.__frequencies = [] # frequencies

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
        return BagIterator(self)

 
class BagIterator:
    
    def __init__(self, b):
        self.__bag = b
        self.__currentPos = 0
        self.__currentFr = 1


    def __next__(self):
        if self.__currentPos == len(self.__bag._BagWithFrequencyPI2__elems):
            raise StopIteration
        currentElem = self.__bag._BagWithFrequencyPI2__elems[self.__currentPos]
        if self.__currentFr < self.__bag._BagWithFrequencyPI2__frequencies[self.__currentPos]:
            self.__currentFr += 1
        else:
            self.__currentPos += 1
            self.__currentFr = 1
        return currentElem         


 #---------------------------------------TESTS and EXAMPLES-----------------------
def createBag():
    b = BagWithFrequencyPI2()
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

def test1ListDict():
    l = [3, 2, 1,7,0,6,4,22,3,56]
    for elem1 in l:
        for elem2 in l:
            print('list ', elem1, ' ', elem2)
            
    d = {}
    for elem in l:
        d[elem] = elem
    for elem1 in d:
        for elem2 in d:
            print('dictionary ', elem1, ' ', elem2)


def test2():
   b = createBag()
   
   iterator = b.__iter__()
   stop = False
   while not stop:
       try:
           elem = iterator.__next__()
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
           

def test4():
    print('Testing modifications on a bag with frequency')
    #see what happens if we add an element to the bag, while iterating over it.
    #CASE 1 - add element 
    # b1 = createBag()
    # for elem in b1:
    #     if elem % 2 == 0:
    #         b1.add(111)
    #     print(elem)
    
    #CASE 2 - add the current element again if even - INFINITE LOOP
    # b2 = createBag()
    # for elem in b2:
    #     if elem % 2 == 0:
    #         b2.add(elem)
    #     print(elem)   

    #CASE 3 - remove the current element
    #b3 = createBag()
    #print("bag");
    #for elem in b3:
    #    print(elem)
    #    b3.remove(elem)



def test4List():
    print('Testing modifications on a list')
    #CASE 1 - add element to the end
    # l1 = [3, 2, 1,7,0,6,4,28,3,56]
    # for elem in l1:
    #     if elem% 2 == 0:
    #         l1.append(111)
    #     print(elem)
    # #CASE 2 - add element to the beginning - INFINITE LOOP
    # l2 = [3, 2, 1,7,0,6,4,22,3,56]
    # for elem in l2:
    #     if elem% 2 == 0:
    #         l2.insert(0, 111)
    #     print(elem)
    # CASE 3 - remove the current element
    #l3 = [3, 2, 1,7,0,6,4,22,3,56, 11]
    #for elem in l3:
    #    print(elem)
    #    l3.remove(elem)

def test4Dict():
    print('Testing modifications on a dictionary')
    #CASE 1 - change value
    l = [3, 2, 1,7,0,6,4,28,3,56]
    d1 = {}
    for e in l:
        d1[e] = -e 
    for elem in d1:
        print(elem)
        if elem% 2 == 0:
            d1[elem] = 111
    
    print(d1)
    #CASE 2 - add new key
    #d2 = {}
    #l2 = [1, 5, 10, 15, 20, 25, 30]
    #for e in l2:
    #    d2[e] = e
    #for elem in d2:
    #    print(elem)
    #    if elem% 2 == 0:
    #        d2[elem+1] = 111
         #CASE 3 - add and remove
    d3 = {}
    l3 = [1, 5, 10, 15, 20, 25, 30]
    for e in l3:
        d3[e] = e
    for elem in d3:
        print(elem)
        if elem% 2 == 0:
            d3[elem+1] = 111
            del d3[elem]
            
    


test1()
test1ListDict()            
test2()
test3()           
test4()
test4List()           
test4Dict()
