from datetime import datetime, timedelta, time

class WhichTime:

	def __init__(self, u=0):
		self.now = datetime.now()
		self.u = u

	def Clock(self):
		pertime = self.now + timedelta(hours=self.u)
		return pertime.time().hour

    
	def Period(self):
		i = self.Clock()

		if 0 <= i < 6:
			print('утро')

		elif 6 <= i < 12:
			print('день')

		elif 12 <= i < 18:
			print('вечер')

		elif 18 <= i < 24:
			print('ночь')



t1 = WhichTime(int(input('Введите часовой пояс (UTC): ')))
t1.Period()