import random
from collections import deque
from party import Party
from adventurer import Adventurer, Equipment, EquipmentList
from adventurer_class import AdventurerClass, AdventurerClassList
from building_list import BuildingList

class Town():


	def __init__(self):
		# self.resources = {"Space": 5, "Population": 0, "Gold": 1000000000, "Wood": 1000000000, "Stone": 1000000000, "Iron": 1000000000, "Crystal": 1000000000}
		self.resources = {"Space": 5, "Population": 0, "Gold": 100, "Wood": 0, "Stone": 0, "Iron": 0, "Crystal": 0}
		self.parties = deque()
		self.buildings = self._generate_buildings()
		self.adventurer_classes = self._generate_adventurer_classes()
		self.equipment = self._generate_equipment()
		self.generate_party() #placeholder

	def _generate_buildings(self):
		buildings = {}
		for building in BuildingList.building_list:
			buildings[building.name] = building
		return buildings

	def _generate_adventurer_classes(self):
		adventurer_classes = {}
		for adventurer_class in AdventurerClassList.adventurer_class_list:
			adventurer_classes[adventurer_class.name] = adventurer_class
		return adventurer_classes

	def _generate_equipment(self):
		equipment = {}
		for equip in EquipmentList.equipment_list:
			equipment[equip] = 0
		return equipment

	def get_next_party(self):
		self.generate_party() #placeholder
		return self.parties.popleft()

	def generate_party(self): #placeholder 
		party = Party(self.generate_adventurer())
		self.parties.append(party)

	def generate_adventurer(self): #placeholder
		adventurer_class = self._random_class()
		adventurer = Adventurer(self.starting_adven_level(adventurer_class), adventurer_class, self._random_heroic())
		adventurer.equip_items(self.equipment)

		return [adventurer]

	def starting_adven_level(self, adventurer_class):
		level = self.buildings["Adventurer's Guild"].number
		if adventurer_class.name == "Brawler":
			level += self.buildings["Tavern"].number
		if adventurer_class.name == "Swordsman":
			level += self.buildings["Barracks"].number
		if adventurer_class.name == "Archer":
			level += self.buildings["Archery Range"].number
		return level

	def _random_class(self):
		weighter = {}
		weighter["Peasant"] = 10 + self.buildings["House"].number
		weighter["Brawler"] = 10 * self.buildings["Tavern"].number
		weighter["Swordsman"] = 10 * self.buildings["Barracks"].number
		weighter["Archer"] = 10 * self.buildings["Archery Range"].number

		total_weight = 0
		for weight in weighter.values():
			total_weight += weight

		result = random.randint(0, total_weight)

		for adventurer_class, weight in weighter.items():
			result -= weight
			if result <= 0:
				return self.adventurer_classes[adventurer_class]


	def _random_heroic(self):
		if self.buildings["Statue of the Goddess"].number > random.randint(0, 100):
			return True
		return False