'''
Created on Nov 7, 2014

@author: esokolyanskaya
'''
import random

class BullsAndCows():
                    
    def __init__(self):
        digits = 5
        ourfile = "text.txt"
        mynum = self.generator(digits)
        self.writefile(mynum, ourfile)
        self.getsize(ourfile)
        self.analyse(ourfile)  
 
    def generator(self):
        first = 10**(self-1)
        last = 10**self-1
        b=str(random.randint(first,last))
        print(b)
        return b
            
    def writefile(self, mynum):
        f = open(self, 'at')
        f.write(mynum + '\n')
        f.close()
    
    
    def getsize(self):    
        f = open(self, 'rt')
        fd = f.readlines()
        print ('size of file: ' + str(len(fd)))
        f.close()
        
    def analyze(self):
        f = open(self, 'rt')
        fd = f.readlines()
        for line in fd: 
            if len(line)-1==2: 
                print ("result: " + line) 
            else: 
                print ('my guess: ' + line)

        
digits = 5
ourfile = "text.txt"
mynum = BullsAndCows.generator(digits)
BullsAndCows.writefile(ourfile, mynum)
BullsAndCows.getsize(ourfile)
BullsAndCows.analyze(ourfile)

    
        