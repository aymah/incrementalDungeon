import random

class Adventurer():

	def __init__(self, level, adventurer_class, heroic):
		self.level = level
		self.adventurer_class = adventurer_class
		self.heroic = heroic
		self.name = "Chobo #" + str(random.randint(1,10000000))
		self.max_hp = self._randomize_hp(level, adventurer_class) * (1 + int(heroic))
		self.curr_hp = self.max_hp
		self.str = self._randomize_str(level, adventurer_class) * (1 + int(heroic))

	def _randomize_hp(self, level, adventurer_class):
		base = random.randint(80 + level * 8, 120 + level * 12)
		return int(base * adventurer_class.stat_mods["HP"])

	def _randomize_str(self, level, adventurer_class):
		base = random.randint(80 + level * 8, 120 + level * 12)
		return int(base * adventurer_class.stat_mods["Str"])