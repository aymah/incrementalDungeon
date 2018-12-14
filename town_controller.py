from town import Town

class TownController():

	def __init__(self):
		self.town = Town()

	def update_state(self):
		self.update_gold()

	def update_gold(self):
		added_gold = self.calculate_gold_income()
		self.town.resources["Gold"] += added_gold

	def calculate_gold_income(self):
		return 1