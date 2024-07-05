import random
import timeit


#generate an array with nrElems unique random numbers between 1 and maxValue
def randomUniqueArray(nrElems, maxValue):
    result = []
    options = []
    for i in range(1, maxValue+1):
        options.append(i)
    random.shuffle(options)
    for i in range(nrElems):
        result.append(options[i])
    return result

#generate an array with nrElems random numbers between 0 and maxValue-1
def randomArray(nrElems, maxValue):
    result = []
    for i in range(nrElems):
        val = random.randint(0, maxValue)
        result.append(val)
    return result

#count how many elements from list l can be found in the container cont
def testContainer(cont, l):
    count = 0
    for elem in l:
        if elem in cont:
            count = count + 1
    return count 

#measures the running time of testContainer for a given container and list 
def timeAlg(cont, testList):
    startTime = timeit.default_timer()
    res = testContainer(cont, testList)
    endTime = timeit.default_timer()
    return endTime - startTime, res


#tests the running time for nrElems elems, repeated nrRepetitions times.
def testCase(nrElems, nrRepetitions=5):
    counts = []
    timesList = []
    timesDict = []
    for i in range(nrRepetitions):
        elems = randomUniqueArray(nrElems, nrElems * 2) 
        lcont = []
        dcont = {}
        for elem in elems:
            lcont.append(elem)
            dcont[elem]= elem
        # initialization of elems2 decides if we are in scenario 1, 2 or 3. 
        #For scenario 1, elems2 should be initialized by randomArray(nrElems, nrElems * 2)
        #For scenario 2, elems2 = elems2
        #This is scenario 3
        elems2 = []
        for elem in elems:            
            elems2.append(elem * -1)
        
        time1, count1 = timeAlg(lcont, elems2)
        time2, count2 = timeAlg(dcont, elems2)
        
        assert(count1 == count2)
        timesList.append(time1)
        timesDict.append(time2)
        counts.append(count2)
    print(' Time for list: ', sum(timesList)/ nrRepetitions)
    print(' Time for dict: ', sum(timesDict)/ nrRepetitions)
    print(' Average count: ', sum(counts)/nrRepetitions)

testCase(200000, 5)