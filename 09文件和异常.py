# #从文件中读取数据
# #读取整个文档
# '''
# pi_digits.txt:

# 3.1415926535
# 8979323846
# 2643383279
# '''
# #使用with关键字 在不需要访问时将文件关闭 也可以open() close() 打开或关闭文件
# with open('pi_digits.txt') as file_object:			#open()函数打开文件，并将open()赋给file_object   应该就是别名的意思
# 	contents = file_object.read()					#read()函数读取全部内容 到达文件末尾时 返回一个空字符串 多显示一个空行
# print(contents)
# #print(open('pi_digits.txt').read())				#我直接打印open().read()也可以打印出来


# file_path = 'pi_digits.txt'							#文件路径   可以使相对路径 也可以是绝对路径
# with open(file_path) as file_object:
# 	contents = file_object.read()
# print(contents)



# #逐行读取
# file_path = 'pi_digits.txt'
# with open(file_path) as file_object:
# 	for line in file_object:				#for循环逐行输出
# 		print(line)							#发现空行更多了

# with open(file_path) as file_object:
# 	for line in file_object:
# 		print(line.strip())					#strip()函数将空行去除







# #创建一个包含文件各行内容的列表
# file_path = 'pi_digits.txt'
# with open(file_path) as file_object:
# 	lines = file_object.readlines()

# for line in lines:
# 	print(line.rstrip())

# #使用文件的内容
# pi_string = ''
# for line in lines:
# 	pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))










# #书籍配套资源地址：https://pan.baidu.com/s/1qYukGPnS6d8Jydqy_DEpFg  提取码：yfvh
# #一百万位的π "..\《Python编程：从入门到实践（第2版）》随书下载资料\源代码文件\chapter_10\pi_million_digits.txt"
# ##包含一百万位的大型文件

# file_path = 'pi_million_digits.txt'

# with open(file_path) as file_object:
# 	lines = file_object.readlines()

# pi_string = ''
# for line in lines:
# 	pi_string += line.strip()

# print(f"{pi_string[:52]}...")
# print(len(pi_string))

# #查看圆周率前一百万位有没有你的生日
# your_birthady = input("Enter your brithday, in the from yymmmdd:")
# if your_birthady in pi_string:
# 	print("Your birthday appears in the first million digits of pi.")
# else:
# 	print("Your birthday does not appears in th first million digits of pi.")





# #写入文件
# #写入空文件
# file_name = 'programming.txt'

# with open(file_name,'w') as file_object:			#在打开文件时传递一个实参‘w’进入写模式(覆盖原本的内容)  ;‘r’读模式 ‘a’附加模式 ‘r+’读写模式
# 	file_object.write("I love programming")
# 	file_object.write("I love programming 002")
# #附加到文件
# with open(file_name,'a') as file_object:			#附加模式 不会删除文件已存在的内容
# 	file_object.write("\tI love programming")







#异常
#处理ZeroDivisionError异常
#print(5/0)				#报错：ZeroDivisionError: division by zero

# #使用try-except代码块
# try:
# 	print(5/0)
# except ZeroDivisionError:					#如果引发ZeroDivisionError异常 就输出这条提示信息
# 	print("You can't divide by zero!")


# #使用异常避免崩溃
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
# 	first_number = input("\nFirst number: ")
# 	if first_number == 'q':
# 		break
# 	second_number = input("Second number: ")
# 	if second_number == 'q':
# 		break
# 	# answer = int(first_number) / int(second_number)			#当second_number为0时 引发ZeroDivisionError异常 程序崩溃无法继续运行
# 	# print(answer)
# 	try:
# 		answer = int(first_number) / int(second_number)			#使用try-except 避免程序崩溃
# 	except ZeroDivisionError:
# 		print("You can't divide by zero!")
# 	else:
# 		print(answer)




# #处理FileNotFoundError异常
# file_name = 'alice.txt'
# # with open(file_name,encoding='utf-8') as f:
# 	# print(f.read())						#报错：FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
# try:
# 	with open(file_name,encoding='utf-8') as f:
# 		print(f.read())
# except FileNotFoundError:
# 	print(f"Sorry, the file {file_name} does not exist.")





# #导入下载资料里面的['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
# #分析文本
# title = 'Alice in wonderland'
# print(title.split())			#split()函数将字符串拆分成单词 存到列表里

# #计算alice有多少单词
# file_name = 'alice.txt'
# try:
# 	with open(file_name,encoding='utf-8') as f:
# 		contents = f.read()
# except FileNotFoundError:
# 	print(f"Sorry, the file {file_name} does not exist.")
# else:
# 	words = contents.split()
# 	num_words = len(words)
# 	print(f"The file {file_name} has about {num_words} woeds.")




# #使用多个文件
# def count_words(filename):
# 	try:
# 		with open(filename,encoding='utf-8') as f:
# 			contents = f.read()
# 	except FileNotFoundError:
# 		pass							#静默失败 什么都不做 pass 还能充当占位符 允许以后会进行某些操作
# 	else:
# 		words = contents.split()
# 		num_words = len(words)
# 		print(f"The file {filename} has about {num_words} words.")

# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt','abc.txt', 'little_women.txt']
# for filename in filenames:
# 	count_words(filename)




# #存储数据
# #使用json.dump() json.load()
# import json

# number = [2,3,4,5,11,13]

# filename = 'numbers.json'			#文件名json表示json格式存储数据
# with open(filename,'w') as f:
# 	json.dump(number,f)				#json.dump()接受两个实参 要存储的数据 以及可用于存储数据的文件对象

# with open(filename) as f:
# 	number = json.load(f)			#json.load()函数将json读取到内存中
# print(number)




# #保存和读取用户生成的数据
# import json
# username = input("What is your name?")

# filename = 'username.json'
# with open(filename,'w') as f:
# 	json.dump(username,f)
# 	print(f"We'll remember you when you come back, {username}!")
# with open(filename) as f:
# 	username = json.load(f)
# 	print(f"Welcome back, {username}.")







# #如果存在username.json就说明运至少行过一次 直接输出问候语就行
# #如果不存在username.json就 输入用户名 新建一个json
# import json
# filename = 'username.json'
# try:
# 	with open(filename) as f:
# 		username = json.load(f)
# except FileNotFoundError:
# 	username = input("What is your name?")
# 	with open(filename,'w') as f:
# 		json.dump(username,f)
# 		print(f"We'll remember you when you come back, {username}!")
# else:
# 	print(f"Welcome back, {username}")







# #重构:原来的代码可以正常运行
# import json
# def greet_user():
# 	"""问候用户，并指出其名字。"""
# 	filename = 'username.json'
# 	try:
# 		with open(filename) as f:
# 			username = json.load(f)
# 	except FileNotFoundError:
# 		username = input("What is your name? ")
# 		with open(filename, 'w') as f:
# 			json.dump(username, f)
# 			print(f"We'll remember you when you come back, {username}!")
# 	else:
# 		print(f"Welcome back, {username}!")
# greet_user()



# #重构:但是通过将其划分不同的部分 还可以改进   能让代码啊更加清晰、更易于理解、更容易拓展
# import json
# def get_stored_username():
# 	"""如果存储了用户名，就获取它。"""
# 	filename = 'username.json'
# 	try:
# 		with open(filename) as f:
# 			username = json.load(f)
# 	except FileNotFoundError:
# 		return None
# 	else:
# 		return username
# def greet_user():
# 	"""问候用户，并指出其名字。"""
# 	username = get_stored_username()
# 	if username:
# 		print(f"Welcome back, {username}!")
# 	else:
# 		username = input("What is your name? ")
# 		filename = 'username.json'
# 		with open(filename, 'w') as f:
# 			json.dump(username, f)
# 			print(f"We'll remember you when you come back, {username}!")
# greet_user()



import json
def get_stored_username():
	"""如果存储了用户名，就获取它。"""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username
def get_new_username():
	"""提示用户输入用户名。"""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
		return username
def greet_user():
	"""问候用户，并指出其名字。"""
	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")
greet_user()
