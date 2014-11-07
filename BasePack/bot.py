'''
Created on Nov 7, 2014

@author: esokolyanskaya
'''

class MyClass(object):
    '''
    classdocs
    '''
    
    somestr = "Some phrase"
    
    def prn(self): 
        a = self.__class__
        print (a)

    prn(somestr)  

    def __init__(self, params):
        '''
        Constructor
        '''
        