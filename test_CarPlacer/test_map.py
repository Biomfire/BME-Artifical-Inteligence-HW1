import unittest
from CarPlacer import map as m
from CarPlacer import car as c


class TestMapConstructor(unittest.TestCase):
    def setUp(self):
        self.testMap = m.Map(1, 1)
        self.testMap2 = m.Map(1, 2)
        self.testMap3 = m.Map(2, 2)
        self.testMap4 = m.Map(4, 4)

    def test_constructor(self):
        self.assertEqual(self.testMap.sizeX, 1)
        self.assertEqual(self.testMap.sizeY, 1)

        self.assertEqual(self.testMap4.sizeX, 4)
        self.assertEqual(self.testMap4.sizeY, 4)

    def test_constructor2(self):
        self.assertEqual(self.testMap2.sizeX, 1)
        self.assertEqual(self.testMap2.sizeY, 2)

    def test_constructor3(self):
        self.assertEqual(self.testMap3.sizeX, 2)
        self.assertEqual(self.testMap3.sizeY, 2)


class TestMapGetCar(unittest.TestCase):
    def setUp(self):
        self.testMap = m.Map(4, 4)

    def test_getcar_no_car(self):
        if self.testMap.getCar(0, 0) is not None:
            self.fail("car is not None")

    def test_placeCar_oneSized_car(self):
        self.testMap.placeCar(0, 0, c.Car(1, 1, 1))
        self.assertEqual(self.testMap.getCar(0, 0).getId(), 1)

    def test_placeCar_2ySized_car_at_0(self):
        self.testMap.placeCar(0, 0, c.Car(1, 2, 1))
        self.assertEqual(self.testMap.getCar(0, 0).getId(), 1)
        self.assertEqual(self.testMap.getCar(0, 1).getId(), 1)

    def test_placeCar_2xSized_car_at_0(self):
        self.testMap.placeCar(0, 0, c.Car(2, 1, 1))
        self.assertEqual(self.testMap.getCar(0, 0).getId(), 1)
        self.assertEqual(self.testMap.getCar(1, 0).getId(), 1)

    def test_placeCar_at_0(self):
        self.testMap.placeCar(0, 0, c.Car(3, 3, 1))
        for i in range(3):
            for j in range(3):
                self.assertEqual(self.testMap.getCar(i, j).getId(), 1)

    def test_placeCar_at_0_2(self):
        self.testMap.placeCar(0, 0, c.Car(4, 2, 1))
        for i in range(3):
            for j in range(2):
                self.assertEqual(self.testMap.getCar(i, j).getId(), 1)

    def test_placeCar_at_random_place(self):
        self.testMap.placeCar(1, 1, c.Car(2, 2, 1))
        for i in range(2):
            for j in range(2):
                self.assertEqual(self.testMap.getCar(1+i, 1+j).getId(), 1)
