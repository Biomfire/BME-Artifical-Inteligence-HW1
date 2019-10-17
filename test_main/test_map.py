import unittest
from main import map as m


class Test_Map_Constructor(unittest.TestCase):
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
