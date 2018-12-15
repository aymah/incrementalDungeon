class AdventurerClass():

	def __init__(self, name, stat_mods):
		self.name = name
		self.stat_mods = stat_mods

class AdventurerClassList():
	adventurer_class_list = [ \
	AdventurerClass("Peasant", {"HP": 1.0, "Str": .75}), \
	AdventurerClass("Brawler", {"HP": 1.2, "Str": 1.2}), \
	AdventurerClass("Swordsman", {"HP": 1.0, "Str": 1.0}), \
	AdventurerClass("Archer", {"HP": .6, "Str": 1.5})]