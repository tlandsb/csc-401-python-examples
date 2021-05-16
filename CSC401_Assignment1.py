##Trey Landsburg
##CSC 401 - ASSIGNMENT ONE – SUMMER SESSION 2019
##Professor Joseph (Yosef) Mendelsohn, M.D.
##7/27/2019

##Problem #1:
lstNumbers = [23,4,-23,107,72,-14,4]
def firstLastHigher (numberlist):
    '''returns the higher number of the first and last elements in a list'''
    firstNumber=int(numberlist[0])
    ##print("The first number is",firstNumber)
    lastNumber=int(numberlist[-1])
    ##print("The last number is",lastNumber)
    if firstNumber > lastNumber:
        return firstNumber
    else:
        return lastnumber
print('Testing problem 1: Expect 23.')
print(firstLastHigher(lstNumbers))

##Problem #2:
def circleGeometry(diameter):
    '''returns area of the circle for a given diameter'''
    radius=float(.5*diameter)
    areaCircle=float(3.14*radius**2)
    return areaCircle
print('\nTesting geometry problem: Expect a string with area about 7.07')
print( circleGeometry(3) )

 
##Problem #3:
def isStringLengthEven(stringword):
    '''determines whether or not the length of a string is odd or even'''
    if len(stringword)%2==0:
        return True
    else:
        return False
        
print('\nTesting word length problem: Expect True, then False.')
print(isStringLengthEven('hi'))
print(isStringLengthEven('bye'))


##Problem #4:
lstStrings = ['hello','goodbye','Tom Cruise is weird.','Gryffindor rules','ABCD']
def checkStringLength(integercompare, stringelement):
    '''determines whether or not the length of a string is larger than a given integer'''
    stringelement.sort()
    stringelement.sort(key=len, reverse=False)
    for i in stringelement:
        if(len(i))>integercompare:
            return True            
        else:
            return False                   
print("\nProblem 4")
print( checkStringLength(3,lstStrings) )
print( checkStringLength(4,lstStrings) )







