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
		self.weapon = Weapon("Bare Fists", "Any", {"Atk": 1.0})

	def _randomize_hp(self, level, adventurer_class):
		base = random.randint(80 + level * 8, 120 + level * 12)
		return int(base * adventurer_class.stat_mods["HP"])

	def _randomize_str(self, level, adventurer_class):
		base = random.randint(20 + level * 2, 30 + level * 3)
		return int(base * adventurer_class.stat_mods["Str"])

	def get_dps(self):
		return int(self.str * self.weapon.stat_mods["Atk"])

	def get_ehp(self):
		return self.max_hp

	def equip_weapon(self, equipment, weapons):
		for name, amount in equipment.items():
			if amount > 0 and weapons[name].adventurer_class_name == self.adventurer_class.name:
				equipment[name] -= 1
				self.weapon = weapons[name]

class Weapon():

	def __init__(self, name, adventurer_class_name, stat_mods, craft_time = 50):
		self.name = name
		self.adventurer_class_name = adventurer_class_name
		self.stat_mods = stat_mods
		self.craft_time = craft_time
		self.craft_progress = 0


class WeaponList():

	weapon_list = [ \
	Weapon("Bare Fists", "Any", {"Atk": 1.0}), \
	Weapon("Wooden Sword", "Swordsman", {"Atk": 1.7}), \
	Weapon("Wooden Gauntlets", "Brawler", {"EHP": 1.1, "Atk": 1.1}), \
	Weapon("Wooden Bow", "Archer", {"Atk": 2.5})]
