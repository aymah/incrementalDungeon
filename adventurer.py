import random

medium_armor_type = ["Brawler", "Swordsman"]
light_armor_type = ["Archer"]

class Adventurer():

	def __init__(self, level, adventurer_class, heroic):
		self.level = level
		self.adventurer_class = adventurer_class
		self.heroic = heroic
		self.name = "Chobo #" + str(random.randint(1,10000000))
		self.max_hp = self._randomize_hp(level, adventurer_class) * (1 + int(heroic))
		self.curr_hp = self.max_hp
		self.str = self._randomize_str(level, adventurer_class) * (1 + int(heroic))
		self.equipment = {}
		self.equipment["Weapon"] = Equipment("Weapon", "Bare Fists", "Any", {"Atk": 1.0}, 0)

	def _randomize_hp(self, level, adventurer_class):
		base = random.randint(80 + level * 8, 120 + level * 12)
		return int(base * adventurer_class.stat_mods["HP"])

	def _randomize_str(self, level, adventurer_class):
		base = random.randint(20 + level * 2, 30 + level * 3)
		return int(base * adventurer_class.stat_mods["Str"])

	def get_dps(self):
		return int(self.str * self._calc_atk_stats())


	def _calc_atk_stats(self):
		mult = 1.0
		for equip in self.equipment.values():
			if "Atk" in equip.stat_mods:
				mult *= equip.stat_mods["Atk"]
		return mult

	def get_ehp(self):
		return int(self.curr_hp * self._calc_ehp_stats())

	def _calc_ehp_stats(self):
		mult = 1.0
		mult += self.get_armor() / 100
		return mult

	def get_armor(self):
		armor = 0
		for equip in self.equipment.values():
			if "Armor" in equip.stat_mods:
				armor += equip.stat_mods["Armor"]
		return armor

	def get_mitigation(self):
		armor = self.get_armor()
		return 1 - (armor / (100 + armor))

	def equip_items(self, equipment):
		self._equip_item("Weapon", equipment)
		self._equip_item("Chest", equipment)

	def _equip_item(self, slot, equipment):
		for equip, amount in equipment.items():
			if amount > 0 and equip.slot == slot and self.adventurer_class.name in equip.adventurer_class_names:
				equipment[equip] -= 1
				self.equipment[slot] = equip

class Equipment():

	def __init__(self, slot, name, adventurer_class_names, stat_mods, craft_time = 50):
		self.slot = slot
		self.name = name
		self.adventurer_class_names = adventurer_class_names
		self.stat_mods = stat_mods
		self.craft_time = craft_time
		self.craft_progress = 0


class EquipmentList():

	equipment_list = [ \
	Equipment("Weapon", "Bare Fists", "Any", {"Atk": 1.0}, 0), \
	Equipment("Weapon", "Wooden Sword", ["Swordsman"], {"Atk": 1.9}), \
	Equipment("Weapon", "Wooden Gauntlets", ["Brawler"], {"Armor": 20, "Atk": 1.1}), \
	Equipment("Weapon", "Wooden Bow", ["Archer"], {"Atk": 2.5}), \
	Equipment("Chest", "Wooden Breastplate", medium_armor_type, {"Armor": 50}), \
	Equipment("Chest", "Wooden Tunic", light_armor_type, {"Armor": 30})]
