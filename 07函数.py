# ##定义函数
# def green_user():			#利用def关键字声明函数
# 	'''显示简单的问候语'''
# 	print("hello !")		#green_user()函数内容

# green_user()				#调用green_user()函数






# ##向函数中传递参数
# def green_user(username):			#利用def关键字声明有参函数
# 	'''显示简单的问候语'''
# 	print(f"hello, {username}!")		#green_user()函数内容

# green_user("张三")				#调用green_user(username)函数 传递参数 “张三”
# ##如上 def声明变量时的username是函数的形参 即调用此函数时需要传递的值
# ##下面调用时的 "张三" 是实参 即实际上使用的值 将实参赋值给形参




# ##传递实参
# def describe_pet(animal_type,pet_name):
# 	print(f"\nI have a {animal_type}.")
# 	print(f"My {animal_type}'s name is {pet_name}")

# #位置实参 即传递实参时 位置与形参一一对应
# describe_pet('hamster','harry')
# describe_pet("dog",'taidi')					#函数可多次调用

# #关键字实参 使用形参名=实参 与位置无关
# describe_pet(animal_type = "cat",pet_name="xiaobai")
# describe_pet(pet_name="xiaobai",animal_type = "cat")




# ##默认值传参 在函数定义时 设置一个默认值
# def describe_pet(animal_type,pet_name='ahui'):
# 	print(f"\nI have a {animal_type}.")
# 	print(f"My {animal_type}'s name is {pet_name}")

# describe_pet(animal_type='pig')						##存在默认值时 无实参传入时就输出默认值
# describe_pet(animal_type='pig',pet_name="abai")		##有实参传入时 以实参为主





# ##返回值
# def get_formatted_name(first_name,last_name):
# 	full_name = f'{first_name} {last_name}'
# 	return full_name.title()						##使用return关键字 将函数结果返回

# musician = get_formatted_name('jimi','hendrix')		##使用变量接受函数的返回值
# print(musician)




# ##让实参变成可循的	例如不一定所有人的名字都有中间的部分
# def get_formatted_name(first_name,last_name,min_name=''):	#设置中间部分默认值为空
# 	if min_name:											#若中间值不为空 即有实参输入
# 		full_name = f'{first_name} {min_name} {last_name}'
# 	else:													#若中间值为空 即没有实参输入
# 		full_name = f'{first_name} {last_name}'
# 	return full_name.title()

# musician = get_formatted_name('jimi','hendrix')
# print(musician)
# musician = get_formatted_name('jimi','hendrix','min')
# print(musician)




# #返回字典
# def build_person(first_name,last_name,age=None):
# 	if age:
# 		person = {'first_name':first_name,'last_name':last_name,'age':age}
# 	else:
# 		person = {'first_name':first_name,'last_name':last_name}
# 	return person

# musician = build_person('jimi','hendeix')
# print(musician)
# musician = build_person('jimi','hendeix',25)
# print(musician)




# #函数结合while循环
# def get_formatted_name(first_name,last_name):
# 	full_name = f"{first_name} {last_name}"
# 	return full_name.title()

# while True:
# 	print('\nPlease tell me your name:')
# 	print('enter "q" at any time to quit.')
# 	f_name = input('first_name:')
# 	if f_name =='q':
# 		break
# 	l_name = input('last_name:')
# 	if l_name =='q':
# 		break
# 	formatted_name = get_formatted_name(f_name,l_name)
# 	print(formatted_name)





# ##传递列表
# def green_user(names):
# 	for name in names:
# 		msg = f'hello {name}'
# 		print(msg)

# usernames = ['abc','gggg','duanduang']
# green_user(usernames)



# ##列表传递时 函数对列表的操作是永久性的 原来的usernames列表也会改变
# def green_user(names):
# 	while names:
# 		print(names.pop())	##删除列表最后一个元素
# 	print(f'names:{names}')

# usernames = ['abc','gggg','duanduang']
# green_user(usernames)
# print(f'usernames:{usernames}')



# ##如果不想修改源列表 可在传递实参时 添加[:] 只把值传给形参
# def green_user(names):
# 	while names:
# 		print(names.pop())	##删除列表最后一个元素
# 	print(f'names:{names}')

# usernames = ['abc','gggg','duanduang']
# green_user(usernames[:])
# print(f'usernames:{usernames}')






# #传递任意个参数
# def make_pizza(*toppings):						##使用*创建一个名为toppings的空元组 接收若干个实参
# 	print('\nMaking a pizza with the following toppings:')
# 	for topping in toppings:
# 		print(f'-{topping}')

# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')



# #结合使用位置实参和传递任意个参数
# def make_pizza(size,*toppings):
# 	print(f'\nMaking a {size}-inch pizza with the following toppings:')
# 	for topping in toppings:
# 		print(f'-{topping}')

# make_pizza(6,'pepperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')




# #结合使用关键字实参和传递任意个参数
# def build_profile(first,last,**user_info):					##**创建一个空字典
# 	user_info['first_name'] = first
# 	user_info['last_name'] = last
# 	return user_info

# user_profile = build_profile('albert','einstein',localtion='princeton',field = 'physics')
# print(user_profile)






# #导入整个模块
# import pizza
# '''
# pizza.py 里面的内容：
# def make_pizza(size,*toppings):
#   print(f'\nMaking a {size}-inch pizza with the following toppings:')
#   for topping in toppings:
#       print(f'-{topping}')
# '''
# pizza.make_pizza(6,'pepperoni')
# pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')




# '''
# test.py 里面的内容：
# def make_pizza(size,*toppings):
#     print(f'\nMaking a {size}-inch pizza with the following toppings:')
#     for topping in toppings:
#         print(f'-{topping}')

# def hello():
#     print('hello world')
# '''
# #导入模块里特定的函数
# from test import hello          #导入test.py中的hello()函数
# hello()


# ##别名
# from test import hello as hi         #hello() 别名 hi()
# hi()
# import test as test_hello_and_pizza          #模块test别名为test_hello_and_pizza
# test_hello_and_pizza.hello()


# #导入模块中所有函数   与导入整个模块来说 导入的全部函数 可以直接使用函数 不用'模块名.函数()'
# from test import *
# hello()
# make_pizza(6,'pepperoni')


##函数编写指南
##形参和实参的‘=’两边不要添加空格     我上边就有添加空格的 这是一个问题 需要修改
##原因： PEP8 建议一行代码不要超过79个字符 添加空格的话就不太好了

