"""
codejam_2017_qual_c.py

Toilet filling problem

You have N + 2 stalls, with guards filling the 2 at the end.

S people fill the stalls, making sure to maximise distance between them and
another person every time they choose it.

When the last person enters their stall, lets calculate the
max distance from them to their next stall, and min distance from
them to their next stall
"""

class ToiletSimulator(object):
	def __init__(self, total_stalls, num_people):
		self.total_stalls = total_stalls
		self.num_people = num_people

	def split_people(self):
		self._stall_dist = {self.total_stalls: 1}
		num_people_left = self.num_people
		print "starting with", self._stall_dist, num_people_left
		while num_people_left > 0:
			stall_dist_max, count_at = self.find_and_remove_stall_dist_max()

			max_dist, min_dist = self.divide_stall_dist(stall_dist_max)

			self.add_to_stall_dist(max_dist, min_dist, count_at)

			print self._stall_dist, max_dist, min_dist, count_at, stall_dist_max, num_people_left
			num_people_left -= count_at

		print "finishing with ", num_people_left

		return max_dist, min_dist

	@staticmethod
	def divide_stall_dist(stall_dist_max):
		max_dist = min_dist = stall_dist_max / 2
		if stall_dist_max % 2 == 0:
			min_dist = min_dist - 1
		return max_dist, min_dist

	def find_and_remove_stall_dist_max(self):
		stall_dist_max = max(self._stall_dist.keys())
		count_at = self._stall_dist[stall_dist_max]
		del self._stall_dist[stall_dist_max]
		return stall_dist_max, count_at

	def add_to_stall_dist(self, max_dist, min_dist, count_at):
		if max_dist not in self._stall_dist:
			self._stall_dist[max_dist] = 0
		if min_dist not in self._stall_dist:
			self._stall_dist[min_dist] = 0
		self._stall_dist[max_dist] = self._stall_dist[max_dist] + count_at
		self._stall_dist[min_dist] = self._stall_dist[min_dist] + count_at


def find_stall_details(total_stalls, num_people):
	"""
	Roughly divide distance by 2 whenever x > 2 ^ x
	"""
	print "total_stalls, num_people", total_stalls, num_people
	ret = ToiletSimulator(total_stalls, num_people).split_people()
	print ret
	return ret


def read_input_file(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()

	output = []
	for line in lines[1:]:
		total_stalls, num_people = line.split(' ')
		total_stalls = int(total_stalls)
		num_people = int(num_people)
		max_dist, min_dist = find_stall_details(total_stalls, num_people)
		output.append("%d %d" % (max_dist, min_dist))

	with open(filename[:-3] + ".out", 'w') as f:
		for i, line in enumerate(output):
			f.write("Case #" + str(i + 1) + ": " + line + "\n")

if __name__ == '__main__':
	#find_stall_details(5, 4)

	read_input_file("C-small-practice-1.in")
	read_input_file("C-small-practice-2.in")
	read_input_file("C-large-practice.in")

