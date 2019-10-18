import unittest

from CarPlacer import car


class TestCarMethods(unittest.TestCase):
    def setUp(self):
        self.testcar = car.Car(1, 2, 1)

    def test_Constructor(self):
        self.assertEqual(self.testcar.sizeX, 1)
        self.assertEqual(self.testcar.sizeY, 2)

    def test_rotate(self):
        self.testcar.rotate()
        self.assertEqual(self.testcar.sizeX, 2)
        self.assertEqual(self.testcar.sizeY, 1)


class TestCarRotate(unittest.TestCase):
    def setUp(self):
        self.testcar = car.Car(1, 2, 1)
        self.testcar2 = car.Car(1, 4, 2)
        self.testcar3 = car.Car(2, 2, 3)
        self.testcar4 = car.Car(2, 5, 4)

    def test_rotate_not_null(self):
        self.assertEqual(self.testcar.getSize(), 2)

    def test_rotate_correct_value(self):
        self.assertEqual(self.testcar.getSize(), 2)

    def test_rotate_correct_value2(self):
        self.assertEqual(self.testcar2.getSize(), 4)

    def test_rotate_correct_value3(self):
        self.assertEqual(self.testcar3.getSize(), 4)

    def test_rotate_correct_value4(self):
        self.assertEqual(self.testcar4.getSize(), 10)

class TestCargetId(unittest.TestCase):
    def setUp(self):
        self.testcar = car.Car(1, 2, 1)
        self.testcar2 = car.Car(1, 4, 2)
        self.testcar3 = car.Car(2, 2, 3)
        self.testcar4 = car.Car(2, 5, 4)

    def test_getId_not_null(self):
        self.assertEqual(self.testcar.getId(), 1)

    def test_getId_correct_value(self):
        self.assertEqual(self.testcar.getId(), 1)

    def test_getId_correct_value2(self):
        self.assertEqual(self.testcar2.getId(), 2)

    def test_getId_correct_value3(self):
        self.assertEqual(self.testcar3.getId(), 3)

    def test_getId_correct_value4(self):
        self.assertEqual(self.testcar4.getId(), 4)


if __name__ == '__main__':
    unittest.main()
