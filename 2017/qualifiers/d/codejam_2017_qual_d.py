"""
codejam_2017_qual_d.py

fashion show

We have a fashion show where there are specific rules about whether or not a
stand is allowed.

Fashion stands are NxN sized.

We have 3 model types,
- + are worth 1 point
- x are worth 1 point
- o are worth 2 points

for any row or column, any 2 models must have at least one +
for any diagonal, any 2 models must have at least one x

When receiving a fashion stand, add as many models, or upgrade any of the ./x
models to o, such that we maximise the value of the overall matrix.
"""


class FashionStand(object):
	def __init__(self, size):
		self.size = size
		self.models = []
		self.new_models = []

	def _check_valid(self):
		for i in range(self.size):
			if self.get_row_count(i) > 1:
				return False

			if self.get_col_count(i) > 1:
				return False

			if self.get_diag1_count(i) > 1:
				return False

			if self.get_diag2_count(i) > 1:
				return False

	def try_upgrade_model(self, model):
		old_type = model.model_type
		if old_type == 'o':
			return
		model.model_type = 'o'
		if self._check_valid():
			if model not in self.new_models:
				self.new_models.append(model)
		else:
			model.model_type = old_type

	def try_add_model(self, model):
		if len(self.get_all_models(self.model_pos_fn(model.x, model.y))) > 0:
			return
		self.models.append(model)
		if self._check_valid():
			self.new_models.append(model)
		else:
			self.models.pop(-1)

	def get_all_models(self, filter_fn):
		return filter(filter_fn, self.models)

	def model_pos_fn(self, x, y):
		def fn(model):
			return model.x == x and model.y == y
		return fn

	def diag1_fn(self, diag1):
		def fn(model):
			return model.x + model.y == diag1 and model.model_type == 'x'
		return fn

	def diag2_fn(self, diag2):
		def fn(model):
			return model.x - model.y == diag2 and model.model_type == 'x'
		return fn

	def row_fn(self, row):
		def fn(model):
			return model.y == row and model.model_type == '+'
		return fn

	def col_fn(self, col):
		def fn(model):
			return model.x == col and model.model_type == '+'
		return fn

	def valid_candidate_for_x(self, x, y):
		return self.get_row_count(y) == 0 and\
			self.get_col_count(x) == 0 and\
			self.get_diag1_count(x + y) <= 1 and\
			self.get_diag2_count(x - y) <= 1

	def valid_candidate_for_plus(self, x, y):
		return self.get_row_count(y) <= 1 and\
			self.get_col_count(x) <= 1 and\
			self.get_diag1_count(x + y) == 0 and\
			self.get_diag2_count(x - y) == 0

	def try_addition_candidates(self):
		for x in range(self.size):
			for y in range(self.size):
				if self.valid_candidate_for_x(x, y):
					self.try_add_model(Model('x', x, y))
				elif self.valid_candidate_for_plus(x, y):
					self.try_add_model(Model('+', x, y))

	def try_upgrade_candidates(self):
		row_candidates = []
		col_candidates = []
		diag1_candidates = []
		diag2_candidates = []
		for i in range(self.size):
			if self.get_row_count(i, typelist=['+']) > \
					1 + self.get_row_count(i):
				row_candidates.append(i)
			if self.get_col_count(i, typelist=['+']) > \
					1 + self.get_col_count(i):
				col_candidates.append(i)
			if self.get_diag1_count(i, typelist=['x']) > \
					1 + self.get_diag1_count(i):
				diag1_candidates.append(i)
			if self.get_diag2_count(i, typelist=['x']) > \
					1 + self.get_diag2_count(i):
				diag2_candidates.append(i)

		for row in row_candidates:
			for model in self.get_all_models(self.row_fn(row)):
				self.try_upgrade_model(model)
		for col in col_candidates:
			for model in self.get_all_models(self.col_fn(col)):
				self.try_upgrade_model(model)
		for diag1 in diag1_candidates:
			for model in self.get_all_models(self.diag1_fn(diag1)):
				self.try_upgrade_model(model)
		for diag2 in diag2_candidates:
			for model in self.get_all_models(self.diag2_fn(diag2)):
				self.try_upgrade_model(model)

	def calculate_new_models(self):
		old_new_model_len = len(self.new_models)
		print "starting calculation", self.size, self.models
		while True:
			print "trying addition"
			self.try_addition_candidates()
			print "trying upgrade"
			self.try_upgrade_candidates()
			if len(self.new_models) == old_new_model_len:
				break
			else:
				old_new_model_len = len(self.new_models)
		return self.print_output()

	def get_new_style(self):
		style = 0
		for model in self.new_models:
			if model.model_type == 'o':
				style += 2
			else:
				style += 1
		return style

	def print_output(self):
		ret = "%d %d\n" % (self.get_new_style(), len(self.new_models))
		for model in self.new_models:
			ret += "%s %d %d\n" % (model.model_type, model.x, model.y)
		return ret

	def get_row_count(self, row, typelist=['x', 'o']):
		ret = 0
		for model in self.models:
			if model.y == row and model.model_type in typelist:
				ret += 1
		return ret

	def get_col_count(self, col, typelist=['x', 'o']):
		ret = 0
		for model in self.models:
			if model.x == col and model.model_type in typelist:
				ret += 1
		return ret

	def get_diag1_count(self, diag, typelist=['+', 'o']):
		ret = 0
		for model in self.models:
			if model.x + model.y == diag and model.model_type in typelist:
				ret += 1
		return ret

	def get_diag2_count(self, diag, typelist=['+', 'o']):
		ret = 0
		for model in self.models:
			if model.x - model.y == diag and model.model_type in typelist:
				ret += 1
		return ret

	def add_model(self, model):
		self.models.append(model)


class Model(object):
	def __init__(self, model_type, x, y):
		self.model_type = model_type
		self.x = int(x)
		self.y = int(y)

	def __repr__(self):
		return "<model: %s, %d, %d>" % (self.model_type, self.x, self.y)


def read_input_file(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()

	output = []

	line_count = 1
	for i in range(int(lines[0])):
		size, model_count = lines[line_count].split(' ')
		line_count += 1
		stand = FashionStand(int(size))
		for j in range(int(model_count)):
			model_type, x, y = lines[line_count].split(' ')
			line_count += 1
			stand.add_model(Model(model_type, int(x), int(y)))
		output.append("%s" % stand.calculate_new_models())

	with open(filename[:-3] + ".out", 'w') as f:
		for i, line in enumerate(output):
			f.write("Case #" + str(i + 1) + ": " + line)


if __name__ == '__main__':
	read_input_file("D-small-practice.in")
	#read_input_file("D-large-practice.in")

