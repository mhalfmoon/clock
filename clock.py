class Clock:
	def __init__(self,hour,minute):
		self.hour = hour
		self.minute = minute
		self.roll()		

	def __eq__(self,other):
		return (self.hour == other.hour and self.minute == other.minute)

	def __str__(self):
		return(self.format_h()+':'+self.format_m())

	def roll(self):
		self.roll_m()
		self.roll_h()

	def roll_h(self):	
		self.hour = self.hour%24

	def roll_m(self):
		self.hour += self.minute/60
		self.minute = self.minute%60

	def format_h(self):
		return(str(self.hour).zfill(2))

	def format_m(self):
		return(str(self.minute).zfill(2))
	
	def add(self,min):
		self.minute += min
		self.roll()
		return self
