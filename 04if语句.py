#一个简单的示例
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#条件测试
#检查是否相等
car = 'bmw'
print(car == 'bmw')
print(car == 'audi')

#检查是否相等时是否忽略大小写
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

#检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies!':
    print("Hold the anchovies")



#数值比较
age = 18
print(age == 18)
print(age == 19)

#if-else
age = 19
if age >20:
    print("age > 20")
else:
    print("20 > age")

#if-elif-else
age = 19
if age >20:
    print("age > 20")
elif age > 18:
    print("20 > age > 18")
else:
    print("18 > age")



cars = ['audi','bmu','subaru','toyota']
for car in cars:
    if car == 'bmu':
        print(car.title())
    else:
        print(car.upper())
num = 5
print("bmu" in cars)                    ##使用in判断元素是否在列表中
print("bmu" not in cars)                ##使用not in判断元素是否不包含在列表中
print(cars[0] == "bmu" or num == 5)     ##使用or表示或判断
print(cars[1].lower() == "bmu")         ##忽略大小写
print(cars[1]=="bmu" and num == 5)      ##使用and表示与判断
print(cars[1]=="bmu")
print(num == 5)








