class SortedList(list):
	def extend(self, value):
		super().extend(value)
		self.sort()
	def append(self, value):
		super().append(value)
		self.sort()

x = SortedList()
x.extend([7, 4, 6, 1, -7])

print(x)
