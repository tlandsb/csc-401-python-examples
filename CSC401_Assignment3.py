##Trey Landsburg
##CSC 401 - ASSIGNMENT THREE – SUMMER SESSION 2019
##Professor Joseph (Yosef) Mendelsohn, M.D.
##8/10/2019

##Problem #1:
##Pseudocode:
##Create file connection
##Read the file into python
##Create holding objects
##Split the list by comma
##Read the file by each item in the list, assign the first item as key
##in a dictionary and the corresponding lines as the values.

def createStudentDict():
    '''opens this file and populates a dictionary with all of the students'''
    try:
        infile=open("students.csv","r")
        data=infile.readlines()
        infile.close()
    except(IOException):
        print("There was a problem opening the file.")
     # print("this is the read in data: ", data)
    list_keys=[]
    list_values=[]
    dictionary={}

##Get list of dictionary values
    for i in range(len(data)):
        line=data[i].replace("\n","").split(",")
        line[2]=int(line[2])
        dictionary[line[0]]=line[1:4]
    return dictionary
print(createStudentDict())


##Problelm #2:
def searchStudentDictionary():
    '''searches the dictionary by student key'''
    while True:        
        # print("this is the read in data: ", data)
        dctStudents = createStudentDict()
        list_keys=[]
        list_values=[]
        dictionary={}
        final_keys=[]
        print()       
        print("Here is a list of keys in your dictionary: ")
        
        for j in dctStudents.keys():
            print(j, end='\t')
        print()
        uservalue=input("Enter a key, when finished type 'done': ")
        if uservalue.lower()=="done":
            break
        print()
        try:
            print('Name: {0}\nAge: {1}\nOccupation: {2}'.format(dctStudents[uservalue][0], dctStudents[uservalue][1], dctStudents[uservalue][2]))
        except (KeyError):
            print("That student is not in the class.")
searchStudentDictionary()      

