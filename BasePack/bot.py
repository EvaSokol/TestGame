'''
Created on Nov 7, 2014

@author: esokolyanskaya
'''
import random

class BullsAndCows(object):
                    
    def __init__(self):
        self.digits = 5
        self.ourfile = "text.txt"
        self.attlist = []
        self.trycount = 0
        self.result = 00
       
    def checkdifferent(self, number):
        for i in range(0, len(number), 1):
            for j in range(i+1, len(number), 1):
                if number[i]==number[j]:
                    return False
        return True
    
    def generator(self, digits):
        first = 10**(digits-1)
        last = 10**digits-1
        b=str(random.randint(first,last))
        while self.checkdifferent(b) == False:
            b=str(random.randint(first,last))     
#        print(b)
        return b
    
    def genattempts(self, digits):
        for num in range(10**(digits-1), 10**digits-1, 1):
            if self.checkdifferent(str(num))==True:
                self.attlist=self.attlist + [num]
#         f = open('attempts.txt', 'wt')
#         for l in self.attlist:
#             f.write(str(l) + ' ')
#         f.close()
#         print ("attlist: " + str(len(self.attlist)))
              
    def writefile(self, filename, data):
        f = open(filename, 'at')
        f.write(data + '\n')
        f.close()
    
#     def getsize(self, filename):    #numbers of strings in file - maybe will be needed
#         f = open(filename, 'rt')
#         fd = f.readlines()
#         print ('size of file: ' + str(len(fd)))
#         f.close()
    
    def genresponse(self, attempt):
        mytry = str(attempt)
        bulls=0
        cows=0
        for i in range(0, len(mytry), 1):
            if mytry[i] == self.secret[i]:
                bulls+=1
        for i in range(0, len(mytry), 1):
            for j in range(0, len(mytry), 1):
                if (mytry[i]==self.secret[i] and i!=j):
                    cows+=1
#        print ("Mytry: " + mytry + " Bulls: " + str(bulls) + " Cows: " + str(cows))
        self.writefile(self.ourfile, str(bulls) + str(cows))
        
    def resultprocessing(self, result):
        print ('Result from file: ' + str(result))    
        
    def analyze(self, filename, digits):
        f = open(filename, 'rt')
        fd = f.readlines()
        line = fd[-1]
        if len(line)-1==2: 
            self.resultprocessing(line)
        elif len(fd[-1])-1==digits: 
            print ('Last line containes 5 digits')
        else: 
            print ('!!! Data format error: ' + line)
#        print('last line: ' + fd[-1])
     
    def cleanlist(self, result):
        for num in self.attlist:
            if self.genresponse(num) != self.result:
                self.attlist.remove(num)
         

A = BullsAndCows()    #Create class object
A.secret = A.generator(A.digits)    #Generate number to guess
print('Secret number: ' + A.secret)   #Print secret number
A.writefile(A.ourfile, A.secret)     # Write secret to file -             to remove
mytry = A.generator(A.digits)       #Generate first attempt
A.result = A.genresponse(mytry)        # Generate result of first attempt
A.genattempts(A.digits)         # Generate the attempts list 
#A.writefile(A.ourfile, A.res)
#A.getsize(A.ourfile)    #to remove
#A.analyze(A.ourfile, A.digits)        #Wait to duel game
print('before cleaning: ' + str(len(A.attlist)))
A.cleanlist(A.result)
print('after cleaning: ' + str(len(A.attlist)))


      
