'''
Created on 5 oct. 2017

@author: Juan
'''
                              
def getValueList():                   
    return [2, 4, 4, 5, 7, 10, 23, 25, 64]

#Complexity: O(N)
def loop(N):
    print("asdasfasdfsf")
    counter = 0;
    while counter < N:
        print(counter)
        print("asdasfasdfsf")
        counter = counter + 1

# Complexity: O(N*N)
def createAllPairs(N):
    x = 0;
    y = 0;
    while x < N:
        y = 0
        while y < N :
            print(x, y)
            y = y + 1
        x = x + 1

# Complexity: O(N)
def factorial(N):
    if N == 1:
        return 1
    return N * factorial(N - 1)

# Complexity: O(N)
def containsNeedle(needle, valueList):
    for value in valueList:
        if value == needle:
            return True
    return False

# Complexity: O(log2 N)
def binarySearch(valueList, needle, min, max):
    midpoint = (max + min) // 2
    if (len(valueList) > 0) and (valueList[midpoint] == needle):
        return midpoint
    if min >= max:
        return -1
    if valueList[midpoint] > needle:
        return binarySearch(valueList, needle, min, midpoint - 1)
    return binarySearch(valueList, needle, midpoint + 1, max)
    

def main():
    valueList = getValueList()
    # seleccionar del 1 al 5
    selectFunction = 5
    N = 8 
    if selectFunction==1:
        loop(N)
    elif selectFunction==2:
        createAllPairs(N)
    elif selectFunction==3:
        fact = factorial(N)
        print("Factorial " + str(N) + " = " + str(fact))
    elif selectFunction==4:
        buscar = 25
        found = containsNeedle(buscar, valueList)
        print("Number " + str(buscar) + " found " + found)
    elif selectFunction==5:
        buscar = 64
        position = binarySearch(valueList, buscar, 0, len(valueList)-1)
        if position == -1:
            print("not found")
        else:
            print("Number " + str(buscar) + " found at position : " + str(position))
            
#Ejecutar
main()