
VERY_LOW, LOW, MEDIUM, HIGH = range(4)

class Task:
	def __init__(self, name: str, duration: int, priority: int):
		self.name = name
		self.duration = duration
		self.priority = priority

	# getters
	def get_name(self) -> str: return self.name
	def get_duration(self) -> int: return self.duration
	def get_priority(self) -> int: return self.priority

	# setters
	def set_name(self, name):
		self.name = name
	def set_duration(self, duration):
		self.duration = duration
	def set_priority(self, priority):
		self.priority = priority

