import os

from CarPlacer.map import Map
from CarPlacer.car import Car
f = open(os.path.realpath('../test_inputs/test2'))
#END
carlist = []
input = f.readline().split("\t")
m = Map(int(input[0]), int(input[1]))
for _ in range(int(f.readline())):
    input = f.readline().split("\t")
    carlist.append(Car(int(input[0]), int(input[1]), _ + 1))
carlist.sort(reverse=True)
donecar = []

for car in carlist:
    done = False
    for y in range(m.sizeY):
        if done:
            donecar.append(car)
            break
        for x in range(m.sizeX):
            if m.placeCar(x, y, car):
                # TODO remove variable from loop
                done = True
                break
            else:
                car.rotate()
                if m.placeCar(x, y, car ):
                    done = True
                    break
                else:
                    car.rotate()
m.print()