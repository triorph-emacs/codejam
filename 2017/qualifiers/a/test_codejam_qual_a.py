"""
test_codejam_qual_a_funcs.py
"""

import unittest
from codejam_2017_qual_a import Pancakes, PancakeOrder


class TestPancakes(unittest.TestCase):
	def test_check_complete(self):
		self.assertTrue(Pancakes("++++").check_complete())
		self.assertFalse(Pancakes("--+").check_complete())
		self.assertFalse(Pancakes("+--").check_complete())
		self.assertFalse(Pancakes("--").check_complete())
		self.assertTrue(Pancakes("+++++++++").check_complete())

	def test_perform_flip(self):
		self.assertEqual(str(Pancakes("-+++-").perform_flip(3, 1)), "-----")
		self.assertEqual(str(Pancakes("+++++-").perform_flip(2, 2)), "++--+-")

class TestPancakesOrders(unittest.TestCase):
	def test_workout_pancake_flip(self):
		self.assertEqual(PancakeOrder("---+-++-", 3).workout_pancake_flip(), 3)
		self.assertEqual(PancakeOrder("+++++", 4).workout_pancake_flip(), 0)
		self.assertEqual(PancakeOrder("-+-+-", 4).workout_pancake_flip(), "IMPOSSIBLE")

	def test_get_all_permutations(self):
		permutations = PancakeOrder("+++++++", 4)._get_all_permutations(3)
		ret = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
		for i, permutation in enumerate(permutations):
			self.assertEqual(permutation, ret[i])

		permutations = PancakeOrder("+++++", 3)._get_all_permutations(2)
		ret = [[0, 1], [0, 2], [1, 2]]
		for i, permutation in enumerate(permutations):
			self.assertEqual(permutation, ret[i])

		permutations = PancakeOrder("+++++", 1)._get_all_permutations(3)
		ret = [[0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 2, 3], [0, 2, 4],
			[0, 3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
		for i, permutation in enumerate(permutations):
			self.assertEqual(permutation, ret[i])
