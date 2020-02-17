

class Ability():
	def __init__(self, name, weapon_types, stats):
		self.name = name
		self.weapon_types = weapon_types
		self.stats = stats

class AbilityList():
	ability_list = [ \
	Ability("Punch", ["Fist"], {"Atk": 1.0}), \
	Ability("Slash", ["Sword"], {"Atk": 1.0}), \
	Ability("Shoot", ["Bow"], {"Atk": 1.0}), \
	Ability("Test", ["Test"], {"Atk": 1.0})]