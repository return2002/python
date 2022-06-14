# ##列表是啥
# ##列表是一系列按特定顺序排列的元素组成 用[]来表示列表


# bicycles = ['trek','cannondale','redline','specialiazed']
# print(bicycles)												##包括[]在内的全部都会打印出来
# print(bicycles[0])											##通过索引来访问列表内的任意元素 索引从0开始
# print(bicycles[0].title())									##任意元素可以调用前一章所学习的字符串方法

# print(f"My first bicycle was a {bicycles[0].title()}")		##可使用f字符串使用列表中的元素



# ##添加、修改、删除元素

# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'						##将ducati赋值给列表的第一个元素
# print(motorcycles)

# motorcycles.append('ducati')					##append()在列表最后添加元素
# print(motorcycles)

# motorcycles.insert(1,'ducati0***')				##在列表的任意位置添加新元素
# print(motorcycles)


# motorcycles =['honda','yamaha','suzuki']
# print(motorcycles)

# del motorcycles[0]									##del语句删除元素
# print(motorcycles)


# motorcycles =['honda','yamaha','suzuki']
# print(motorcycles)

# popped_motorcycles = motorcycles.pop()				##pop()方法将列表最后一个元素取出 等同于在列表中删除
# print(motorcycles)
# print(popped_motorcycles)

# popped_motorcycles = motorcycles.pop(0)				##pop(0)方法将指定元素取出 等同于在列表中删除
# print(motorcycles)
# print(popped_motorcycles)



# motorcycles = ['honda','yamaha','suzuki','ducati','suzuki']
# print(motorcycles)

# motorcycles.remove('suzuki')							##当不知元素位置时 利用remove()方法根据值进行删除 当存在多个相同的值时 只删除第一个
# print(motorcycles)





# cars = ['bmw','audi','totota','subaru']
# cars.sort()												##sort()方法永久性修改列表排列顺序
# print(cars)

# cars.sort(reverse=True)									##stor(reverse=True) 反序排列
# print(cars)


# cars = ['bmw','audi','totota','subaru']
# print(sorted(cars))											##stored(cars)方法临时修改cars列表排列顺序
# print(cars)

# cars.reverse()												##reverse()方法永久改变顺序 前后倒置
# print(cars)
# cars.reverse()												##再次调用reverse()方法变回原来的顺序
# print(cars)




# cars = ['bmw','audi','toyota','subaru']
# print(len(cars))												##len()确定列表长度
# print(cars[-1])													##索引还能是负数


