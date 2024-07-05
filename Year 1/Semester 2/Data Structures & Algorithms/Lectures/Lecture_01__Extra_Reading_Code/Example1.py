import timeit
import random

#First version-------------------------------------------
def firstVersion(elements):
    maxSum = 0
    for i in range(len(elements)):
        for j in range(i, len(elements)):
            currentSum = 0
            for k in range(i, j+1):
                currentSum += elements[k]
            if currentSum > maxSum:
                maxSum = currentSum
    return maxSum
#Complexity Theta(n^3)

#Second version -------------------------------------------
def secondVersion(elements):
    maxSum = 0
    for i in range(len(elements)):
        currentSum = 0
        for j in range(i, len(elements)):
            currentSum += elements[j]
            if currentSum > maxSum:
                maxSum = currentSum
    return maxSum
#Complexity Theta(n^2)

#Third version----------------------------------------------------
def crossMiddle(elements, left, right):
    middle = (left + right) // 2
    leftSum = 0
    maxLeftSum = 0
    index = middle
    while index >= left:
        leftSum = leftSum + elements[index]
        if leftSum > maxLeftSum:
            maxLeftSum = leftSum
        index = index - 1
    
    rightSum = 0
    maxRightSum = 0
    index = middle + 1
    while index <= right:
        rightSum = rightSum + elements[index]
        if rightSum > maxRightSum:
            maxRightSum = rightSum
        index = index + 1
    return maxLeftSum + maxRightSum
    

def fromInterval(elements, left, right):
    if left == right:
        return elements[left]
    middle = (left + right) // 2
    justLeft = fromInterval(elements, left, middle)
    justRight = fromInterval(elements, middle+1, right)
    acrossMiddle = crossMiddle(elements, left, right)
    return max(justLeft, justRight, acrossMiddle)

def thirdVersion(elements):
    return fromInterval(elements, 0, len(elements)-1)


#Fourth version---------------------------------------------
def fourthVersion(elements):
    maxSum = 0 
    currentSum = 0 
    for i in range(
        len(elements)):
        currentSum += elements[i]
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum
        
#Code to randomly test for correctness--------------------------------------------------------
#generate an array with nrElems random numbers between -1000 and 1000
def randomArray(nrElems):
    result = []
    for i in range(nrElems):
        result.append(random.randint(-1000, 1000))
    return result


def randomTest(nrTests):
    for i in range(nrTests):
        listLength = random.randint(100, 500)
        print('Test ', i, ' list with ', listLength, ' elements')
        testList = randomArray(listLength)
        v1 = firstVersion(testList)
        print('  First version ', v1)
        v2 = secondVersion(testList)
        print('  Second version ', v2)
        v3 = thirdVersion(testList)
        print('  Third version ', v3)
        v4 = fourthVersion(testList)
        print('   Fourth version ', v4)
        assert(v1 == v2)
        assert(v1 == v3)
        assert(v1 == v4)

#randomTest(100)

#Measuring running time---------------------------------------------------------
#Parameters are the algorithm and the list to test on
def timeAlg(algorithm, testList):
    startTime = timeit.default_timer()
    algorithm(testList)
    endTime = timeit.default_timer()
    return endTime - startTime


#run each algorithm nrRepetitions times on a random list with nrElems elems and print the average runtime in the end
#Parameters are the number of elements and how many times to generate a list. 
def testCase(nrElems, nrRepetitions= 5):
    
    firstTimes = []
    secondTimes = []
    thirdTimes = []
    fourthTimes = []
    
    for i in range(nrRepetitions):
        testList = randomArray(nrElems)
        firstTimes.append(timeAlg(firstVersion, testList))
        secondTimes.append(timeAlg(secondVersion, testList))
        thirdTimes.append(timeAlg(thirdVersion, testList))
        fourthTimes.append(timeAlg(fourthVersion, testList))
    
    print('First algorithm: ', sum(firstTimes)/nrRepetitions)
    print('Second algorithm: ', sum(secondTimes)/nrRepetitions)
    print('Third algorithm: ', sum(thirdTimes)/nrRepetitions)
    print('Fourth algorithm: ', sum(fourthTimes)/nrRepetitions)
    

testCase(1000)