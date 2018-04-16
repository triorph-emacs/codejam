"""
test_codejam_qual_c.py
"""

import unittest
from codejam_2017_qual_c import ToiletSimulator

class TestToiletSimulator(unittest.TestCase):
	def setUp(self):
		pass

	def test_full_toilets(self):
		args_list = [(100, 100), (1000, 1000), (3000, 3000)]
		for args in args_list:
			simulator = ToiletSimulator(*args)
			self.assertEqual(simulator.split_people(), (0, 0))

	def test_one_person_left(self):
		args_list = [(100, 99), (1000, 999), (250, 249)]
		for args in args_list:
			simulator = ToiletSimulator(*args)
			self.assertEqual(simulator.split_people(), (0, 0))

	def test_simple_examples(self):
		args_list = [(4, 2), (5, 2), (6, 2), (1000, 1)]
		ret_list = [(1, 0), (1, 0), (1, 1), (500, 499)]
		for args, ret in zip(args_list, ret_list):
			simulator = ToiletSimulator(*args)
			self.assertEqual(simulator.split_people(), ret)
