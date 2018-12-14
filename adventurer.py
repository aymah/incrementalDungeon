import random

class Adventurer():

	def __init__(self, level):
		self.level = level
		self.name = "Chobo #" + str(random.randint(1,10000000))
		self.max_hp = random.randint(80 + level * 8, 120 + level * 12)
		self.curr_hp = self.max_hp
		self.str = random.randint (80 + level * 8, 120 + level * 12)