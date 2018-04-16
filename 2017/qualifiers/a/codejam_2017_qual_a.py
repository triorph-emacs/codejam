"""
codejam_2017_qual_a.py

The pancake flipper

Given a state of pancakes, and an oversized pancake flipper that can flip
exactly N pancakes in a row, how many flips are required to get them all
happy side up, or "IMPOSSIBLE" if not.
"""

class Pancakes(object):
	def __init__(self, pancakes_string):
		self._pancakes_string = str(pancakes_string)

	def reverse(self):
		"""
		Reverse a set of pancakes
		"""
		ret = ""
		for pancake in self._pancakes_string:
			if pancake == "-":
				ret += "+"
			else:
				ret += "-"
		self._pancakes_string = ret

	def __repr__(self):
		return self._pancakes_string

	def __len__(self):
		return len(self._pancakes_string)

	def __getitem__(self, key):
		return self._pancakes_string[key]

	def check_complete(self):
		"""
		Check if a set of pancakes are completely all face up
		"""
		for pancake in self._pancakes_string:
			if pancake != "+":
				return False
		return True

	def flip(self, flipper_size, position):
		"""
		For a set of pancakes with a given flipper size, return
		the resulting pancake set that would arise
		"""
		pancakes_start = self._pancakes_string[0:position]
		flipped_string = self._pancakes_string[position:position + flipper_size]
		pancakes_flipped = Pancakes(flipped_string)
		pancakes_flipped.reverse()
		pancakes_end = self._pancakes_string[position + flipper_size:]
		return Pancakes(pancakes_start + str(pancakes_flipped) + pancakes_end)


class PancakeOrder(object):
	def __init__(self, pancakes, flipper_size):
		self.pancakes = Pancakes(pancakes)
		self.flipper_size = int(flipper_size)

	def get_max_flips(self):
		return len(self.pancakes) - self.flipper_size + 1

	def workout_pancake_flip(self):
		if self.pancakes.check_complete():
			return 0
		else:
			count = self._try_flips()
			if self.pancakes.check_complete():
				return count
			else:
				return "IMPOSSIBLE"

	def _try_flips(self):
		count = 0
		for i in range(self.get_max_flips()):
			if self.pancakes[i] == '-':
				count += 1
				self.pancakes = self.pancakes.flip(self.flipper_size, i)
		return count


def read_input_file(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()

	output = []
	for line in lines[1:]:
		pancakes, flipper_size = line.split(' ')
		order = PancakeOrder(pancakes, flipper_size)
		output.append(order.workout_pancake_flip())

	with open(filename[:-3] + ".out", 'w') as f:
		for i, line in enumerate(output):
			f.write("Case #" + str(i + 1) + ": " + str(line) + "\n")

if __name__ == '__main__':
	read_input_file("A-small-practice.in")
	read_input_file("A-large-practice.in")
