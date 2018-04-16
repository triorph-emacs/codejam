"""
codejam_2017_qual_b.py

Tidy numbers are numbers where the digits are sorted in alphabetical order

e.g. 224466, 123999

NOT e.g. 225560, 1243

We are looking for the largest tidy number that is less than or equal to the
number given
"""

def find_tidy_number(number):
	tidy_number = number
	for i in range(1, len(tidy_number))[::-1]:
		print i, len(tidy_number), tidy_number
		if int(tidy_number[i - 1]) > int(tidy_number[i]):
			start_number = tidy_number[0:i - 1]
			less_number = str(int(tidy_number[i - 1]) - 1)
			end_number = "9" * (len(tidy_number) - i)
			tidy_number = start_number + less_number + end_number

	while tidy_number.startswith('0'):
		tidy_number = tidy_number[1:]

	return tidy_number


def read_input_file(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()

	output = []
	for line in lines[1:]:
		output.append(find_tidy_number(line[:-1]))

	with open(filename[:-3] + ".out", 'w') as f:
		for i, line in enumerate(output):
			f.write("Case #" + str(i + 1) + ": " + str(line) + "\n")

if __name__ == '__main__':
	read_input_file("B-small-practice.in")
	read_input_file("B-large-practice.in")

