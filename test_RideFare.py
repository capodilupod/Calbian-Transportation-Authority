import RideFare
import unittest

class TestAdd(unittest.TestCase):
	def test_findMinSubset(self):
		"""
		Examples from problem statement email
		"""
		result = RideFare.findMinSubset(7, [1, 4, 6])
		self.assertEqual(result, 3)

		result = RideFare.findMinSubset(8, [1, 4, 6])
		self.assertEqual(result, 0)

		result = RideFare.findMinSubset(57, [6, 13, 21, 23, 24])
		self.assertEqual(result, 4)

		"""
		Next two test cases test how permutation can change which gaavos are needed
		"""

		result = RideFare.findMinSubset(9, [1,3,5,2,8])
		self.assertEqual(result, 3)

		result = RideFare.findMinSubset(9, [1,3,2,8,5])
		self.assertEqual(result, 4)

		"""
		Test for 100 sequential number array which does not sum in total to fareCost 
		"""
		sequentialArray = []
		for i in range(1, 101):
			sequentialArray.append(i)

		result = RideFare.findMinSubset(5051, sequentialArray)
		self.assertEqual(result, 0)


	def test_findPieces(self):
		"""
		Examples from problem statement email
		"""

		result = RideFare.findPieces(7, [1,4,6])
		self.assertEqual(result, [1, 6])

		result = RideFare.findPieces(8, [1, 4, 6])
		self.assertEqual(result, [])

		result = RideFare.findPieces(57, [6, 13, 21, 23])
		self.assertEqual(result, [13, 21, 23])


		"""
		Tests for permutations should not affect answer if only one possible combination of given set is there
		"""

		result = RideFare.findPieces(11, [1, 3, 2, 5, 8])
		self.assertEqual(result, [3,8])

		result = RideFare.findPieces(11, [8, 5, 2, 1, 3])
		self.assertEqual(result, [8, 3])

		"""
		Test for 20 sequential number array where whole array is needed to make fareCost
		"""
		sequentialArray = []
		for i in range(1, 26 ):
			sequentialArray.append(i)

		result = RideFare.findPieces(325, sequentialArray)
		self.assertEqual(result, sequentialArray)


if __name__ == '__main__':
    unittest.main()