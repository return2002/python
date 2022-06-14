# magicians = ['alice','david','carolina']
# for magician in magicians:						##使用for()循环遍历整个数组
# 	print(magician)
# 	print(f"\t{'Magician:'+magician.title()}\n")
# print("\n\n")


# for value in range(1,5):							##range(1,5)代表1,2,3,4 并不包含5
# 	print(value)

# numbers = list(range(1,6))							##list()将range(1,6)转换为列表
# print(numbers)

# numbers = list(range(2,11,2))						##range()还能指定步长
# print(numbers)


# squares = []
# for value in range(1,11):
# 	square = value ** 2
# 	squares.append(square)
# print(squares)



# digits = [1,2,3,4,5,6,7,8,9]
# print(min(digits))							##min()最小值
# print(max(digits))							##max()最大值
# print(sum(digits))							##sum()总和

# squares = [value**2 for value in range(1,11)]
# print(squares)



# ##使用列表
# players = ['charles','martina','michael','florence','eli']
# print(players[0:3])											##列表切片
# print(players[:3])
# print(players[3:])

# for player in players[:3]:									##遍历切片
# 	print(player)


# my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods[:]

# print("my_foods:")
# print(my_foods)

# print(f"{'friend_foods:'}")
# print(friend_foods)



# my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods								##这个是将my_foods赋给friend_foods friend_foods指向的是my_foods[:] 同时发生改变
# my_foods.pop()

# print("my_foods:")
# print(my_foods)

# print(f"{'friend_foods:'}")
# print(friend_foods)





##元组		使用()来标识元组 元组不可改变
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[1] = 60			#会报错
#print(dimensions[1])

for dimension in dimensions:
	print(dimension)

dimensions = (300,60)				##虽然元组的值不能改变 但是可以对元组进行重新赋值
for dimension in dimensions:
	print(dimension)



