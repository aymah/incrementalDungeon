from game_settings import GameSettings

class Building():

	def __init__(self, name, cost, cost_multiplier = 1.25):
		self.name = name
		self.cost = cost
		self.cost_multiplier = cost_multiplier
		self.number = 0
		self.button = None
		self.needs_update = True

	def build(self, town):
		can_afford = True
		for resource, amount in self.cost.items():
			if amount > town.resources[resource]:
				can_afford = False
		if can_afford:
			for resource, amount in self.cost.items():
				town.resources[resource] -= amount
			self.number += 1
			self._increment_cost()
			self.needs_update = True


	def _increment_cost(self):
		for resource, amount in self.cost.items():
			self.cost[resource] = int(amount * self.cost_multiplier)

	# def set_name(self, name):
	# 	self.name = name
	# 	if self.button is not None
	# 		self.button.update(self)

	# def set_cost(self, cost):
	# 	self.cost = cost
	# 	if self.button is not None
	# 		self.button.update(self)

	# def set_number(self, number):
	# 	self.number = number
	# 	if self.button is not None
	# 		self.button.update(self)






	# name = property(set_name)
	# cost = property(set_cost)
	# number = property(set_number)