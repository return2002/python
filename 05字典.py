# alien_0 = {'color':'green','points':5}

# print(alien_0['color'])
# print(alien_0['points'])

# print(alien_0)

# #添加键值对
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)




# alien_0 = {'color':'green','points':5}
# print(alien_0)
# #修改字典中的值
# alien_0['color'] = 'red'
# print(alien_0)

# #删除键值对
# del alien_0['color']
# print(alien_0)



# #创建类似对象的字典 调查者喜欢的语言
# favorite_languages = {
# 	'jen': 'python',
# 	'sarah': 'c',
# 	'edward': 'ruby',
# 	'phil': 'python'
# }
# print(favorite_languages)





# aline_0 = {'color':'green','speed':'slow'}
# print(aline_0)

# point_value = aline_0.get('point','no point value assigned')		#当键可能不存在时 应考虑使用get()方法 避开方括号表示
# print(point_value)

# for key,value in aline_0.items():									#遍历所有键值对
# 	print(f'\nKey:{key}')
# 	print(f'Value:{value}')

# for key in aline_0.keys():											#遍历所有的键
# 	print(key)

# for value in aline_0.values():										#遍历所有的值
# 	print(value)




# ##嵌套
# #字典列表
# alien_0 = {'color':'green','points':5}
# alien_1 = {'color':'yellow','points':10}
# alien_2 = {'color':'red',"points":15}

# aliens = [alien_0,alien_1,alien_2]				#列表元素由 字典组成
# for alien in aliens:
# 	print(alien)


# #字典中存储列表
# pizza = {
# 	'crust':'thick',
# 	'toppings':['mushrooms','extra cheese']
# }

# print(f"You ordered a {pizza['crust']}-crust pizza with the followong toppings:")
# for topping in pizza['toppings']:
# 	print('\t'+topping)


#在字典中存储字典
users = {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
	},
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris'
	}
}

for username,user_info in users.items():
	print(f'\nUsername:{username}')
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f'\tFull name:{full_name.title()}')
	print(f'\tLocation:{location.title()}')













