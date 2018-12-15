from dungeon import Dungeon
from town_controller import TownController

class DungeonController():

	def __init__(self, town_window):
		self.dungeon = Dungeon()
		self.town_controller = town_window.town_controller
		self.town = self.town_controller.town
		self.next_party()
		self.next_monster()

	def update_state(self):
		if self.dungeon.curr_party is not None and self.dungeon.curr_monster is not None:
			self._combat_round(self.dungeon.curr_party, self.dungeon.curr_monster)

	def next_party(self):
		self.dungeon.curr_party = self.town.get_next_party()

	def next_monster(self):
		self.dungeon.curr_monster = self.dungeon.get_next_monster()

	def _combat_round(self, party, monster):
		adventurer = party.adventurers[0]
		self._resolve_attack(adventurer, monster)
		if monster.curr_hp <= 0:
			self.town.resources["Gold"] += monster.gold_reward
			self.dungeon.monsters_killed += 1
			self.next_monster()
			return
		self._resolve_attack(monster, adventurer)
		if adventurer.curr_hp <= 0:
			self.dungeon.reset_monster_queue()
			self.next_monster()
			self.next_party()

	def _resolve_attack(self, source, target):
		damage = int(source.get_dps())
		target.curr_hp -= damage
