from collections import deque
from party import Party
from adventurer import Adventurer

class Town():

	def __init__(self):
		self.gold = 0
		self.parties = deque()
		self.generate_party() #placeholder

	def get_next_party(self):
		self.generate_party() #placeholder
		return self.parties.popleft()

	def generate_party(self): #placeholder 
		party = Party(self.generate_adventurer())
		self.parties.append(party)

	def generate_adventurer(self): #placeholder
		return [Adventurer(0)]