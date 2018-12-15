#by extending adventurer class and modifying relevant code, we can probably make it so stat_mods or whatever includes stuff like +levels and +weight for classes
#would really clean stuff up, and make it SUPER easy to add classes, just need to fill out the stuff on the class list and it would be done?

class AdventurerClass():

	def __init__(self, name, stat_mods):
		self.name = name
		self.stat_mods = stat_mods

class AdventurerClassList():
	adventurer_class_list = [ \
	AdventurerClass("Peasant", {"HP": 1.0, "Str": .6}), \
	AdventurerClass("Brawler", {"HP": 1.2, "Str": 1.0}), \
	AdventurerClass("Swordsman", {"HP": 1.0, "Str": 0.8}), \
	AdventurerClass("Archer", {"HP": .6, "Str": .7})]
