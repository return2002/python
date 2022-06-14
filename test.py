class Car:
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

class Battery:
	def __init__(self,battery_size=100):
		self.battery_size = battery_size

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This electricCar can go about {range} miles on a full charge.")


class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()

def make_pizza(size,*toppings):
	print(f'\nMaking a {size}-inch pizza with the following toppings:')
	for topping in toppings:
		print(f'-{topping}')

def hello():
	print('hello world')
