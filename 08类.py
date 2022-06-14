# #创建和使用类
# #创建Dog类
# class Dog:
# 	def __init__(self,name,age):				##方法_init_(),每当根据Dog类创建实例时自动执行 不能写错或省略 self参数不能省略且位于第一位。
# 		self.name = name						#Dog类的属性，可以通过实例进行访问的变量
# 		self.age = age
# 	def sit(self):
# 		print(f'{self.name} is now sitting.')
# 	def roll_over(self):
# 		print(f"{self.name} rolled over!!")

# #访问属性
# my_dog = Dog('willie',6)						#根据类创建实例
# print(f"My dog's name is {my_dog.name}.")		#通过 实例.属性 访问属性值
# print(f"My dog is {my_dog.age} years old.")
# #调用方法
# my_dog.sit()									#通过 实例.方法() 调用方法
# my_dog.roll_over()

# #创建多个实例										#可以根据一个类创建多个实例 每个实例都相互独立
# your_dog = Dog('ahui',3)
# print(f"Your dog's name is {my_dog.name}.")
# print(f"Your dog is {my_dog.age} years old.")
# your_dog.sit()
# your_dog.roll_over()







# #使用类和实例
# #Car类
# class Car:
# 	def __init__(self,make,model,year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		long_name = f"{self.year} {self.make} {self.model}"
# 		return long_name.title()
# 	def read_odometer(self):
# 		print(f"This car has {self.odometer_reading} miles on it")

# 	def update_odometer(self,mileage):
# 		self.odometer_reading = mileage

# 	def update_odometer_02(self,mileage):			##对update_odometer方法的改进，里程表调动时不能回调，即只能往大调
# 		if self.odometer_reading <= mileage:
# 			self.odometer_reading = mileage
# 		else:
# 			print("You can't roll back an odometer!")
# 	def increment_odometer(self,mileage):
# 		self.odometer_reading += mileage



# my_new_car = Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# #直接修改属性的值
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# #通过方法修改属性的值
# my_new_car.update_odometer(999)
# my_new_car.read_odometer()
# #修改值时 添加修改条件限制
# my_new_car.update_odometer_02(998)
# my_new_car.read_odometer()
# my_new_car.update_odometer_02(1000)
# my_new_car.read_odometer()

# #通过方法对属性的值进行递增
# my_new_car = Car('abc','a4',2022)
# print(f'\n{my_new_car.get_descriptive_name()}')
# my_new_car.update_odometer(99_999)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(1_000)
# my_new_car.read_odometer()








# #继承
# class Car:
# 	def __init__(self,make,model,year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0

# 	def get_descriptive_name(self):
# 		long_name = f"{self.year} {self.make} {self.model}"
# 		return long_name.title()
# 	def read_odometer(self):
# 		print(f"This car has {self.odometer_reading} miles on it")

# 	def update_odometer(self,mileage):
# 		self.odometer_reading = mileage

# 	def update_odometer_02(self,mileage):			##对update_odometer方法的改进，里程表调动时不能回调，即只能往大调
# 		if self.odometer_reading <= mileage:
# 			self.odometer_reading = mileage
# 		else:
# 			print("You can't roll back an odometer!")
# 	def increment_odometer(self,mileage):
# 		self.odometer_reading += mileage

# 	def test01(self):								##用来和子类做例子、对照
# 		print("This is Car")

# class ElectricCar(Car):
# 	def __init__(self,make,model,year):
# 		super().__init__(make,model,year)

# 		self.battery_size = 75			##这是ElectricCar独有的属性

# 	def describe_battery(self):
# 		print(f"This car has a {self.battery_size}-kWh battery.")

# 	def test01(self):					##方法重写，父类也存在次方法时，可根据自身需求进行重写 以重写后的方法为准
# 		print("This is ElectricCar")

# my_tesla = ElectricCar('tesla','model s',2020)
# print(my_tesla.get_descriptive_name())			##调用父类中的方法

# my_tesla.describe_battery()						##调用自身的方法

# my_tesla.test01()								##调用重写后的方法





# #将实例用作属性
# class Car:
# 	def __init__(self,make,model,year):
# 		self.make = make
# 		self.model = model
# 		self.year = year

# 	def get_descriptive_name(self):
# 		long_name = f"{self.year} {self.make} {self.model}"
# 		return long_name.title()

# class Battery:									#将电池分离出来 看似麻烦很多 但它使ElectricCar类更整洁 且可以更详细的描述电池
# 	def __init__(self,battery_size=100):
# 		self.battery_size = battery_size

# 	def describe_battery(self):
# 		print(f"This car has a {self.battery_size}-kWh battery.")

# 	def get_range(self):
# 		if self.battery_size == 75:
# 			range = 260
# 		elif self.battery_size == 100:
# 			range = 315
# 		print(f"This electricCar can go about {range} miles on a full charge.")


# class ElectricCar(Car):
# 	def __init__(self,make,model,year):
# 		super().__init__(make,model,year)
# 		self.battery = Battery()

# my_tesla = ElectricCar('tesla','model s',2201)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()








# '''
# test.py里面的内容：
# class Car:
# 	def __init__(self,make,model,year):
# 		self.make = make
# 		self.model = model
# 		self.year = year

# 	def get_descriptive_name(self):
# 		long_name = f"{self.year} {self.make} {self.model}"
# 		return long_name.title()

# class Battery:
# 	def __init__(self,battery_size=100):
# 		self.battery_size = battery_size

# 	def describe_battery(self):
# 		print(f"This car has a {self.battery_size}-kWh battery.")

# 	def get_range(self):
# 		if self.battery_size == 75:
# 			range = 260
# 		elif self.battery_size == 100:
# 			range = 315
# 		print(f"This electricCar can go about {range} miles on a full charge.")


# class ElectricCar(Car):
# 	def __init__(self,make,model,year):
# 		super().__init__(make,model,year)
# 		self.battery = Battery()

# def make_pizza(size,*toppings):
# 	print(f'\nMaking a {size}-inch pizza with the following toppings:')
# 	for topping in toppings:
# 		print(f'-{topping}')

# def hello():
# 	print('hello world')
# '''
# ##导入类
# #导入单个类
# from test import Car

# my_new_car = Car('audi','a4',2019)
# print(my_new_car.get_descriptive_name())

# #导入一个模块的多个类
# from test import Car,ElectricCar,Battery
# my_tesla = ElectricCar('tesla','model s',2201)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# #导入一个模块的所有类
# from test import *
# my_tesla = ElectricCar('tesla','model s',2201)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# ##与导入方法类似 也可以给类起别名
# ##模块中也可以引入模块




#python标准库
from random import randint,choice
print(randint(1,6))					#randint()随机生成一个数

players = ['charles','martina','minchael','florence','eli']
first_up = choice(players)			#choice()随机返回一个元素
print(first_up)










