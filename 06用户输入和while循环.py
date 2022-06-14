# #前言：input()在sublime控制台无效 需要单独设置
#         #PS：sublime 需要安装SublimeREPL插件 参考地址 https://blog.csdn.net/gaocui883/article/details/103972425
# ###下面是我的快捷键设置 Ctrl+b保存之后再运行新窗口 省去单独保存的过程
#         #{
#         #   "keys": ["ctrl+b"],
#         #   "command": "save_all",
#         #},
#         #{ "keys": ["ctrl+b"],
#         #   "caption": "SublimeREPL:Python",
#         #   "command": "run_existing_window_command",
#         #   "args":
#         #   {
#         #      "id": "repl_python_run",
#         #      "file": "config/Python/Main.sublime-menu"
#         #   }
#         #},
# #新打开的运行窗口 可使用Ctrl+w进行关闭
# #**************************************


# ##函数input()的工作原理
# #input("这里是输入提示：")函数可以获取输入字符串 并赋值给 '='之前的变量
# message = input("Tell me something, and I will repeat it back to you:")
# print(message)



# #int()函数 获取数值
# age = input("How old are you?")
# print(type(age))                  ##type(变量名) 函数得到变量类型 此处返回<class 'str'> 即字符类型
# age = int(age)
# print(type(age))                  ##int(变量)将变量类型转换至int类型 此处返回<class 'int'> 即数值类型




# #求模运算   即取余数 例如：4%3 余数为1
# print(4%3)
# print(5%3)
# print(6%3)
# print(7%3)





# ##while循环
# current_number = 1
# while current_number <= 5:            ##while [条件]： 当条件成立时 会一直运行 直至条件不成立
#     print(current_number)
#     current_number += 1



# prompt = '\nTell me something, and I will repeat it back to you:'
# prompt += '\nEnter "quit" to end the program'
# message = ''
# while message != 'quit':				##message不为quit时 一直执行下去
# 	message = input(prompt)
# 	print(message)



# ##使用标志(flag)
# prompt = '\nTell me something, and I will repeat it back to you:'
# prompt += '\nEnter "quit" to end the program'

# active = True						#此处用active当标志 判断是否继续执行
# while active:
# 	message = input(prompt)

# 	if message == 'quit':
# 		active = False
# 	else:
# 		print(message)




# ##使用break退出循环
# prompt = '\nPlease enter the name of a city you have visited:'
# prompt += '\n(Enter "quit" when you are finished.)'

# while True:
# 	city = input(prompt)

# 	if city == 'quit':
# 		break								##break表示结束循环 在此处跳出循环 后面的代码都不会执行
# 	else:
# 		print(f"I'd love to go to {city.title()}")



# ##在循环中使用continue
# current_number = 0
# while current_number < 10:
# 	current_number += 1
# 	if current_number % 2 == 0:				##代表如果current_number是偶数 就结束本次循环
# 		continue							##continue是不执行本次循环中的 后面的代码 直接进入下一次循环 不会使循环结束
# 	print(current_number)


##** 注意 **：
##一定要避免无限循环
##每个while都必须有停止运行的途径





# ##使用while循环处理列表和字典
# #在列表间移动元素
# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []

# while unconfirmed_users:							##当unconfirmed不为空时 一直执行
# 	current_user = unconfirmed_users.pop()			##将最后一个元素取出 赋值给current_user

# 	print(f"Verifying user:{current_user.title()}")
# 	confirmed_users.append(current_user)			##将current_user添加到confirmed列表中

# print(confirmed_users)




# ##删除为特定值的所有列表元素
# unconfirmed_users = ['alice','brian','alice','candace','alice']

# while 'alice' in unconfirmed_users:					##当unconfirmed里存在 alice时 一直执行
# 	unconfirmed_users.remove('alice')				##移除unconfirmed里的一个 alice

# print(unconfirmed_users)




##使用用户输入来填充字典
responses = {}
#定义一个标记
polling_active = True

while polling_active:
	name = input("\nWhat is your name?")
	response = input("which mountain would you like to climb soneday?")
	responses[name] = response

	repeat = input("would you like to let another person respond?(yes/no)")
	if repeat == 'no':
		polling_active = False

print('\n------------POLL RESULTS------------\n')
for name,response in responses.items():
	print(f'{name} would like to climb {response}')



















