import sys
import unittest
import test1

class Prelab04TestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.purchaseDict = test1.getPurchaseReport()
        cls.totalSoldDict = test1.getTotalSold()

    def test_getPurchaseReport(self):

        key, value = 7, 393.34

        expectedValue = value
        actualValue = self.purchaseDict[key]

        self.assertEqual(expectedValue, actualValue)


    def test_getTotalSold(self):

        key, value = 'Nectarines', 49

        expectedValue = value
        actualValue = self.totalSoldDict[key]

        self.assertEqual(expectedValue, actualValue)

    def test_getPurchaseReport2(self):

        key, value = 3, 310.38

        expectedValue = value
        actualValue = self.purchaseDict[key]

        self.assertEqual(expectedValue, actualValue)


    def test_getTotalSold2(self):

        key, value = 'Asparagus', 37

        expectedValue = value
        actualValue = self.totalSoldDict[key]

        self.assertEqual(expectedValue, actualValue)

if __name__ == '__main__':
    unittest.main()
