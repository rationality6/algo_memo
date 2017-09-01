import unittest
from bubble_sort


class Test(unittest.TestCase):

    def testBubblesort(self):
        A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        sorting.bubblesort(A)
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                self.fail("bubblesort method fails.")
