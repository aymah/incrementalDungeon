import random
from ability import Ability


class Monster():

	def __init__(self, level):
		self.level = level
		self.name = "Monster #" + str(random.randint(1,10000000))
		self.max_hp = random.randint(40 + level * 4, 60 + level * 6)
		self.curr_hp = self.max_hp
		self.str = random.randint (10 + level * 1, 15 + int(level * 1.5))
		self.gold_reward = int((self.max_hp * self.str) / 100)
		self.abilities = [Ability("Punch", ["Fist"], {"Atk": 1.0})]


	def get_dps(self):
		return self.str

	def get_mitigation(self):
		return 1

	def get_abilities(self):
		return self.abilities

	def get_ability(self, target):
		return random.choice(self.get_abilities())