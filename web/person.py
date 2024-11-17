class Person:
	def __init__(self, name, age, country, id):
		self.name = name
		self.age = age
		self.country = country
		self.id = id

	def __str__(self):
		return f"Person(name={self.name}, age={self.age}, country={self.country}, id={self.id})"

	def updateAge(self, newAge):
		self.age = newAge
		print(f"in:=> {self.name} updated:=> {self.age}")

timik = Person("timik", 33, "israel", 10)
timor = Person("tamir", 53, "israel", 11)

timik.updateAge(34)
timor.updateAge(54)

print(timik)
print(timor)
