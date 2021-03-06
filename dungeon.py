from collections import deque
from monster import Monster

class Dungeon():

	def __init__(self):
		self.placeholder = 0
		self.curr_party = None
		self.curr_monster = None
		self.monsters = deque()
		self.monsters_killed = 0
		self.last_adventurer = None
		self.greatest_adventurer = None
		self.generate_monster()


	def get_next_monster(self):
		self.generate_monster() #placeholder
		return self.monsters.popleft()

	def generate_monster(self): #placeholder 
		if self.greatest_adventurer is None or self.greatest_adventurer.monsters_killed < self.last_adventurer.monsters_killed:
			self.greatest_adventurer = self.last_adventurer
		self.monsters.append(Monster(self.monsters_killed))

	def reset_monster_queue(self):
		self.monsters = deque()
		self.monsters_killed = 0
		self.generate_monster()
