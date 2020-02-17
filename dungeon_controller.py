from dungeon import Dungeon
from town_controller import TownController

class DungeonController():

	def __init__(self, town_window):
		self.dungeon = Dungeon()
		self.town_controller = town_window.town_controller
		self.town = self.town_controller.town
		self.next_party()
		self.next_monster()
		self.last_attack = None

	def update_state(self):
		if self.dungeon.curr_party is not None and self.dungeon.curr_monster is not None:
			self._combat_round(self.dungeon.curr_party, self.dungeon.curr_monster)

	def next_party(self):
		self.dungeon.curr_party = self.town.get_next_party()

	def next_monster(self):
		self.dungeon.curr_monster = self.dungeon.get_next_monster()

	def get_last_attack(self):
		return self.last_attack

	def _combat_round(self, party, monster):
		adventurer = party.adventurers[0]
		self._resolve_attack(adventurer, monster)
		adventurer.time += 1
		if monster.curr_hp <= 0:
			self.town.resources["Gold"] += monster.gold_reward
			adventurer.monsters_killed += 1
			self.dungeon.monsters_killed += 1
			adventurer.gold_earned += monster.gold_reward
			self.next_monster()
			return
		self._resolve_attack(monster, adventurer)
		if adventurer.curr_hp <= 0:
			adventurer.curr_hp = adventurer.max_hp #might need to replace this with a "reset adventurer" function
			self.dungeon.last_adventurer = adventurer
			self.dungeon.reset_monster_queue()
			self.next_monster()
			self.next_party()

	def _resolve_attack(self, source, target):
		ability = source.get_ability(target)
		raw_damage = int(source.get_dps() * ability.stats["Atk"])
		damage = int(raw_damage * target.get_mitigation())
		target.curr_hp -= damage
		last_attack = {"Attacker": source, "Defender": target, "Ability": ability, "Damage": damage}
