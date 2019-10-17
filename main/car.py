class Car:
    def __init__(self, sizex, sizey):
        self.sizeX = sizex
        self.sizeY = sizey

    def getsizex(self):
        return self.sizeX

    def getsizey(self):
        return self.sizeY

    def rotate(self):
        tmp = self.sizeY
        self.sizeY = self.sizeX
        self.sizeX = tmp

    def getSize(self):
        return self.sizeY*self.sizeX
