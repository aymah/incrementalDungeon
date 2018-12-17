import random

class Monster():

	def __init__(self, level):
		self.level = level
		self.name = "Monster #" + str(random.randint(1,10000000))
		self.max_hp = random.randint(40 + level * 4, 60 + level * 6)
		self.curr_hp = self.max_hp
		self.str = random.randint (10 + level * 1, 15 + int(level * 1.5))
		self.gold_reward = int((self.max_hp * self.str) / 100)


	def get_dps(self):
		return self.str

	def get_mitigation(self):
		return 1