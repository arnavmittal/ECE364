import os
import sys
import uuid
import unittest
from practical1 import *
from datetime import timedelta

def loadPuzzleFiles(path1, path2):
    """
    Load two text files and return them to allow for assertion of their content. A more elegant way to do that is to
    create a custom assertion function: assertTextEqual
    """
    with open(path1, 'r') as firstFile:
        first = firstFile.read()

    with open(path2, 'r') as secondFile:
        second = secondFile.read()

    return first, second

class Lab05TestSuite(unittest.TestCase):

    def setUp(self):
        """
        Create a new file name to use if a test needs so.
        """
        self.targetFilePath = str(uuid.uuid4()) + '.sud'

    def test_checkPythonVersion(self):

        currentVersion = sys.version_info
        self.assertGreaterEqual(currentVersion, (3, 4))

    def test_verifySolution(self):

        with self.subTest(key="good1"):
            actualValue = verifySolution("good1.sud")
            self.assertTrue(actualValue)

        with self.subTest(key="good2"):
            actualValue = verifySolution("good2.sud")
            self.assertTrue(actualValue)

        with self.subTest(key="bad1"):
            actualValue = verifySolution("bad1.sud")
            self.assertFalse(actualValue)

        with self.subTest(key="bad2"):
            actualValue = verifySolution("bad2.sud")
            self.assertFalse(actualValue)

    def test_solvePuzzle(self):

        with self.subTest(key="open1"):

            sourceFileName = "sudoku_open1.sud"
            expectedFileName = "sudoku_solved1.sud"
            targetFileName = str(uuid.uuid4()) + '.sud'

            solvePuzzle(sourceFileName, targetFileName)
            actualValue, expectedValue = loadPuzzleFiles(targetFileName, expectedFileName)
            os.remove(targetFileName)

            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="open2"):

            sourceFileName = "sudoku_open2.sud"
            expectedFileName = "sudoku_solved2.sud"
            targetFileName = str(uuid.uuid4()) + '.sud'

            solvePuzzle(sourceFileName, targetFileName)
            actualValue, expectedValue = loadPuzzleFiles(targetFileName, expectedFileName)
            os.remove(targetFileName)

            self.assertEqual(actualValue, expectedValue)

    def test_getCallersOf(self):

        with self.subTest(key="(707) 825-5871"):
            expectedValue = ['Brooks, Carol', 'Butler, Julia', 'Carter, Sarah', 'Edwards, Rachel', 'James, Randy',
                             'Miller, Aaron', 'Nelson, Louise', 'Rogers, Elizabeth', 'Washington, Annie']
            actualValue = getCallersOf("(707) 825-5871")

            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="(626) 677-3812"):
            expectedValue = ['Bell, Kathryn', 'Davis, Douglas', 'Edwards, Rachel', 'Flores, Andrea', 'Jackson, Doris',
                             'James, Randy', 'Miller, Aaron', 'Nelson, Louise', 'Rogers, Elizabeth', 'Russell, Scott',
                             'Thompson, Michelle', 'Torres, Betty', 'Washington, Annie']
            actualValue = getCallersOf("(626) 677-3812")

            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="(999) 999-9999"):
            expectedValue = []
            actualValue = getCallersOf("(999) 999-9999")

            self.assertEqual(actualValue, expectedValue)

    def test_getCallActivity(self):

        callEntries = getCallActivity()

        with self.subTest(key="Edwards, Rachel"):
            key = "Edwards, Rachel"
            expectedValue = 56, '13:54:46'
            actualValue = callEntries[key]

            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="Russell, Scott"):
            key = "Russell, Scott"
            expectedValue = 35, '08:54:18'
            actualValue = callEntries[key]

            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="Call Count"):

            expectedValue = 1000
            actualValue = sum([count for count, _ in callEntries.values()])

            self.assertEqual(actualValue, expectedValue)

        with self.subTest(key="Total Duration"):

            durationStrings = [duration.split(":") for _, duration in callEntries.values()]
            durationList = [timedelta(hours=int(hh), minutes=int(mm), seconds=int(ss))
                            for hh, mm, ss in durationStrings]
            expectedValue = timedelta(hours=256, minutes=49, seconds=48)
            actualValue = sum(durationList, timedelta())

            self.assertEqual(actualValue, expectedValue)

if __name__ == '__main__' :
    unittest.main()
