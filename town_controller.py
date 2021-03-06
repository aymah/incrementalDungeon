from town import Town

class TownController():

	def __init__(self):
		self.town = Town()

	def update_state(self, dungeon_window):
		self._update_gold()
		self._update_wood()
		self._update_pop()
		self._update_space(dungeon_window)
		self._update_crafting()

	def _update_gold(self):
		added_resource = self._calculate_gold_income()
		self.town.resources["Gold"] += added_resource

	def _calculate_gold_income(self):
		town_hall_level = self.town.buildings["Town Hall"].number
		house_number = self.town.buildings["House"].number
		return town_hall_level * (5 + house_number)

	def _update_wood(self):
		added_resource = self._calculate_wood_income()
		self.town.resources["Wood"] += added_resource

	def _calculate_wood_income(self):
		return self.town.buildings["Lumber Mill"].number

	def _update_pop(self):
		house_number = self.town.buildings["House"].number
		used_pop = self._calculate_used_pop()
		self.town.resources["Population"] = house_number - used_pop

	def _calculate_used_pop(self):
		total_upkeep = 0;
		for building in self.town.buildings.values():
			building_number = building.number
			pop_upkeep = building.cost.get("Population")
			if pop_upkeep is not None:
				total_upkeep += building_number * pop_upkeep
		return total_upkeep

	def _update_space(self, dungeon_window):
		additional_space = 0
		if dungeon_window.dungeon.greatest_adventurer is not None:
			additional_space = dungeon_window.dungeon.greatest_adventurer.monsters_killed
		total_space = 5 + additional_space
		used_space = self._calculate_used_space()
		self.town.resources["Space"] = total_space - used_space

	def _calculate_used_space(self):
		total_upkeep = 0;
		for building in self.town.buildings.values():
			building_number = building.number
			space_upkeep = building.cost.get("Space")
			if space_upkeep is not None:
				total_upkeep += building_number * space_upkeep
		return total_upkeep

	def _update_crafting(self):
		for equip in self.town.equipment.keys():
			if equip.name == "Wooden Gauntlets":
				equip.craft_progress += self.town.buildings["Gauntlet Forge"].number
			if equip.name == "Wooden Sword":
				equip.craft_progress += self.town.buildings["Swordsmith"].number
			if equip.name == "Wooden Bow":
				equip.craft_progress += self.town.buildings["Bowyer"].number
			if equip.name == "Wooden Breastplate":
				equip.craft_progress += self.town.buildings["Armorsmith"].number
			if equip.name == "Wooden Tunic":
				equip.craft_progress += self.town.buildings["Tailor"].number
			if equip.craft_progress >= equip.craft_time:
				equip.craft_progress -= equip.craft_time
				self.town.equipment[equip] += 1


	
