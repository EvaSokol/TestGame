'''
Created on Nov 7, 2014

@author: esokolyanskaya
'''
import random

class MyClass(object):
    '''
    classdocs
    '''

    def generator():
        a=random.randint(10000,99999)
        return a
    
    
    mynum = generator()
    print (mynum)

    def __init__(self, params):
        '''
        Constructor
        '''
        