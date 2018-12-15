from collections import deque
from party import Party
from adventurer import Adventurer
from building_list import BuildingList

class Town():


	def __init__(self):
		self.resources = {"Population": 1, "Gold": 0, "Wood": 0, "Stone": 0, "Iron": 0, "Crystal": 0}
		self.parties = deque()
		self.buildings = self._generate_buildings()
		self.generate_party() #placeholder

	def _generate_buildings(self):
		buildings = {}
		for building in BuildingList.building_list:
			buildings[building.name] = building
		return buildings

	def get_next_party(self):
		self.generate_party() #placeholder
		return self.parties.popleft()

	def generate_party(self): #placeholder 
		party = Party(self.generate_adventurer())
		self.parties.append(party)

	def generate_adventurer(self): #placeholder
		return [Adventurer(self.starting_adven_level())]

	def starting_adven_level(self):
		return self.buildings["Adventurer's Guild"].number