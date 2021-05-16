##Trey Landsburg
##CSC 401 - ASSIGNMENT FOUR – SUMMER SESSION 2019
##Professor Joseph (Yosef) Mendelsohn, M.D.
##8/17/2019

##Problem #1:

class Book(object):

    libraryName='DePaul Library' 
    
    def __init__(self,title='unset',author='unset',edition=-1,checkedOut=None):
        '''docstring'''
        self.title=title
        self.author=author
        self.edition=edition
        self.checkedOut=checkedOut

    def __eq__(self, other):
        '''docstring'''
        return self.title.lower()==other.title.lower() and self.author.lower()==other.author.lower()     

    def checkOut(self):
        '''docstring'''
        self.checkedOut=True
        return True

    def returnBook(self):
        '''docstring'''
        self.checkedOut=False
        return False

    def __str__(self):
        '''docstring'''
        if self.checkedOut==True:
            self.checkedOut="Yes"
        if self.checkedOut==False:
            self.checkedOut="No"
        if self.checkedOut==None:
            self.checkedOut="No"
        s = '***{}***\n\
Title:\t{}\n\
Author: {}\n\
Edition: {}\n\
CheckedOut: {}'.format(Book.libraryName, self.title, self.author, self.edition, self.checkedOut)
        return s        

b1 = Book('Great Expectations','Charles Dickens',3)
b2 = Book('Canterbury Tales','Geoffry Chaucer',1,checkedOut=False)
print(b2.checkOut())  #when we print, Checked Out? should print 'Yes'
b3 = Book('great expectations','charles dickens',3)

print(b1)
print()
print(b2)  #NOTE: 'checkedOut' should indicate 'Yes'
print()
print(b3)
print()
print('Comparing b1 and b3 - should be True:\t', b1==b3)
print('Comparing b2 and b3 - should be False:\t', b2==b3)







