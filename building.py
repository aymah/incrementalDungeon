class Building():

	def __init__(self, name, cost):
		self.name = name
		self.cost = cost
		self.number = 0

	def build(self, town):
		can_afford = True
		for resource, amount in self.cost.items():
			if amount > town.resources[resource]:
				can_afford = False
		if can_afford:
			for resource, amount in self.cost.items():
				town.resources[resource] -= amount
			self.number += 1
