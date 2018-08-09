from Queue import *

class Garage:
    def __init__(self, maxSize):
        self.gSize = maxSize
        self.garage = Queue()

    def entry(self,car):
        self.garage.enqueue(car)

    def exits(self,lPlate):
        return self.garage.removeItem(lPlate)
    
    def isFull(self):
        return self.garage.size() == self.gSize

    def isExist(self,lPlate):
        return self.garage.findItem(lPlate) == True

        
