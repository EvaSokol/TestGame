'''
Created on Nov 7, 2014

@author: esokolyanskaya
# test commit
'''
import random
import time

class BullsAndCows(object):

    def __init__(self):
        self.digits = 5
        self.ourfile = "text.txt"
        self.attlist = []
        self.trycount = 0
        self.result = 00
        self.mytry = 0
       
    def checkdifferent(self, number):
        for i in range(0, len(number), 1):
            for j in range(i+1, len(number), 1):
                if number[i] == number[j]:
                    return False
        return True

    def generator(self, digits):
        a = len(self.attlist)
#        print('Lenght of list: ' + str(a))
        b = random.randint(0, a-1)
        return str(self.attlist[b])
    
    def genattempts(self, digits):
        for num in range(10**(digits-1), 10**digits-1, 1):
            if self.checkdifferent(str(num)):
                self.attlist = self.attlist + [num]
#         f = open('attempts.txt', 'wt')
#         for l in self.attlist:
#             f.write(str(l) + ' ')
#         f.close()
#         print ("attlist: " + str(len(self.attlist)))
              
    def writefile(self, filename, data):
        f = open(filename, 'at')
        f.write(data + '\n')
        f.close()
    
    def getsize(self, filename):    #numbers of strings in file
        f = open(filename, 'rt')
        fd = f.readlines()
        print ('size of file: ' + str(len(fd)))
        f.close()
        return len(fd)
    
    def genresponse(self, att, base):
        max = self.digits
        bulls = 0
        cows = 0
        for y in range(0, max, 1):
            if att[y] == base[y]:
                bulls += 1
        for i in range(0, max, 1):
            for j in range(0, max, 1):
                if att[i] == base[j] and i != j:
                    cows += 1
        return str(cows) + str(bulls)
        
    def resultprocessing(self, result):
        print('Result from file: ' + str(result))
        self.result = str(result)
        
    def analyze(self, filename, digits):
        f = open(filename, 'rt')
        fd = f.readlines()
        line = fd[-1]
        print('Last line contains: ' + str(len(line)))
        if len(line) == 2:
            self.resultprocessing(line)
            return 2
        elif len(fd[-1]) == digits:
            print('Last line contains 5 digits')
            return 5
        else: 
            print('!!! Data format error: ' + line)

    def cleanlist(self, mytry):
        toremove = []
        for num in self.attlist:
            if self.genresponse(mytry, str(num)) != A.result:
                toremove = toremove + [num]
        for r in toremove:
            self.attlist.remove(r)

    def selfgame(self):
        self.genattempts(self.digits)         # Generate the attempts list
        self.secret = self.generator(self.digits)    #Generate number to guess
        print('Secret number: ' + self.secret)
        self.writefile(self.ourfile, "\n" +"New game")
        while len(self.attlist) != 1:
            self.mytry = self.generator(self.digits)       #Generate first attempt
            self.writefile(self.ourfile, self.mytry)
            self.result = self.genresponse(self.mytry, self.secret)        # Generate result of first attempt
            self.writefile(self.ourfile, self.result)
            self.trycount += 1
            print('==================== Attempt number: ' + str(self.trycount))
            print("Mytry: " + self.mytry + " Cows: " + str(self.result[0]) + " Bulls: " + str(self.result[1]))
            #self.writefile(self.ourfile, self.res)
            #self.getsize(self.ourfile)    #to remove
            #self.analyze(self.ourfile, self.digits)        #Wait to duel game
        #    print('before cleaning: ' + str(len(self.attlist)))
            self.cleanlist(self.mytry)
        #    print('after cleaning: ' + str(len(self.attlist)))
        print('You won! It\'s ' + str(self.attlist[0]))
        self.writefile(self.ourfile, 'You won! It\'s ' + str(self.attlist[0]))

    def iguessgame(self):
        self.genattempts(self.digits)
        while len(self.attlist) != 1:
            self.mytry = self.generator(self.digits)
            self.writefile(self.ourfile, self.mytry)
            size = self.getsize(self.ourfile)
            while size == self.getsize(self.ourfile):
                time.sleep(10)
            self.analyze(self.ourfile, self.digits)
            print('before cleaning: ' + str(len(self.attlist)))
            self.cleanlist(self.mytry)
            print('after cleaning: ' + str(len(self.attlist)))
        self.mytry = self.attlist[0]
        self.writefile(self.ourfile, self.mytry)


A = BullsAndCows()
#A.selfgame()
A.iguessgame()

