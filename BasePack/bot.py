'''
Created on Nov 7, 2014

@author: esokolyanskaya
'''
import random
from _ctypes import sizeof

class MyClass(object):
    '''
    classdocs
    '''

    def generator():
        a=random.randint(10000,99999)
        b=str(a)
        return b
     
    mynum = generator()
    print (mynum)
    
    f = open('text.txt', 'at')
    f.write(mynum + '\n')
    f.close()
    
    f = open('text.txt', 'rt')
    fd = f.readlines()
    print ('size of file: ' + str(len(fd)))
   
    f.close()
    
    for line in fd: 
        if len(line)-1==2: 
            print ("result: " + line) 
        else: 
            print ('my guess: ' + line)

        
   

    def __init__(self, params):
        '''
        Constructor
        '''
        