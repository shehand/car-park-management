class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def removeItem(self, item):
        for i in self.items:
            if i == item:
                self.items.remove(item)
            else:
                return False

    def findItem(self, item):
        for i in self.items:
            if i == item:
                return True
            else:
                return False

    def getItem(self, item):
        for Car in self.items:
            if Car.lPlate == item:
                return Car

            
        

