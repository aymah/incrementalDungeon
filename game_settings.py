class GameSettings():

	def __init__(self):
		self.game_width = 1280
		self.game_height = 720
		self.hz = 60
		self.refresh_time = 1000/self.hz
		self.update_time = 1000

	def set_game_width(self, width):
		self.game_width = width

	def set_game_height(self, height):
		self.game_height = height