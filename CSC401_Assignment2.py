##Trey Landsburg
##CSC 401 - ASSIGNMENT TWO – SUMMER SESSION 2019
##Professor Joseph (Yosef) Mendelsohn, M.D.
##8/5/2019

# •	read(), Returns a single  string containing all of the remaining (i.e. unread) contents of the file
# •	readline(), Returns the next line of the file i.e. the text up to and including the newline character ‘\n’
# •	readlines(), Returns a list whose items are the remaining, unread lines of the file.

##Problem #1:
def countLinesWithString(word):
    '''returns how many lines a given string is found on'''
    try:
        infile=open("shakespeare_short.txt","r",encoding='utf-8')
    except:
        print("Sorry was unable to open the file.")
    data=infile.readlines()

    data2 = []
    for i in range(len(data)):
        if word.lower() in data[i].lower():
            data2.append(data[i])
    return len(data2)
print("Testing with RoMeO - should be 41: ", end=" ")
print(countLinesWithString('RoMeO'))
print("Testing with THOU - should be 38: ", end=" ")
print(countLinesWithString('THOU'))

##Problem #2:
def getMonthlySales(person, month):
    '''returns the sales for a given individual and month'''
    try:
        infile=open("widget_sales_with_id.txt", 'r')
    except:
        print("Sorry was unable to open the file.")
    data=infile.readlines()

    for i in data:
        splitData=i.split(",")
        if splitData[0].lower()==person.lower():
            return splitData[month]
print("Testing with Shaggy and 1, should be 2138: ", end=" ")
print(getMonthlySales('shaGGy',1))
print("Testing with Robin Hood and 6, should not return anything (None): ", end=" ")
print(getMonthlySales('Robin Hood',6))
print("Testing with SCRAPPY and 12, should return 2312:", end=" ")
print(getMonthlySales('SCRAPPY',12))






















