class Map:
    def __init__(self, x, y):
        self.sizeX = x
        self.sizeY = y
        self.spaces = [[None] * self.sizeY for i in range(self.sizeX)]

    def print(self):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                car = self.getCar(x, y)
                if car is None:
                    if x == self.sizeX-1:
                        print("0", end='')
                    else:
                        print("0", end='\t')
                else:
                    if x == self.sizeX-1:
                        print(self.spaces[x][y].getId(), end='')
                    else:
                        print(self.spaces[x][y].getId(), end='\t')
            print()

    def getCar(self, x, y):
        return self.spaces[x][y]

    def checkifplaceisfree(self, x, y, car):
        for i in range(car.sizeX):
            for j in range(car.sizeY):
                if x+i > self.sizeX-1 or y+j > self.sizeY-1:
                    return False
                elif self.spaces[x + i][y + j] is not None:
                    return False
        return True

    def placeCarIntoDataParkSpace(self, x, y, car):
        for i in range(car.sizeX):
            for j in range(car.sizeY):
                self.spaces[x + i][y + j] = car

    def placeCar(self, x, y, car):
        if self.checkifplaceisfree(x, y, car):
            self.placeCarIntoDataParkSpace(x, y, car)
            #TODO Do not return
            return True

        else:
            return False