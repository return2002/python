# print("Hello python world!!")

# message = "hello"
# print(message)

# ## python中被引号括起来的都是字符串,"" ''都可以
# print("hello*****")
# print('*****hello')



# ##使用方法修改字符串的大小写

# name = "abd defg"
# print(name.title())			##title()将单词的首字母大写


# name = "Abc Defg"
# print(name.upper())			##upper()将字符串全部大写
# print(name.lower())			##lower()将字符串全部小写


# ##在字符串中使用变量
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"			##引号前加上字母f 会将花括号中的变量替换为其值
# print(full_name)
# print(f"full_name = {full_name}")
# print(f"full_name = {full_name.title()}!")


# ##使用制表符或换行符来添加空白
# print("Python")
# print("\tPython")
# print("P\n\ty\n\t\tt\n\t\t\th\n\t\t\t\to\n\t\t\t\t\tn")		##\n表示换行符,\t表示制表符 


# ##删除空白
# favorite_language = 'python '
# print(f"{favorite_language}**")
# print(f"{favorite_language.rstrip()}**")		##rstrip()能将最右侧的空白去掉

# favorite_language = "  py thon  "
# print(f"{favorite_language}**")
# print(f"{favorite_language.lstrip()}**")		##lstrip()能将最左侧的空白去掉
# print(f"{favorite_language.lstrip().rstrip()}**")
# print(f"{favorite_language.strip()}**")			##strip()同时去除两边的空白



# ##数
# print(3 + 2)
# print(3 - 2)
# print(3 * 2)
# print(3 / 2)
# print(3 + 4*2)				##数的运算符合算数运算法则 先乘除后加减

# print(3 ** 2)				##**表示平方关系
# print(3 + 2.0)			
# print(3 * 2.0)
# print(4 / 2)				##只要有浮点数参与计算 结果总是浮点数   任意两数相除 结果总是浮点数

# universe_age = 14_000_000_000
# print(universe_age)			##当数字很大时 为了方便易读 可添加下划线 打印时并不会将下划线打印出来




# ##同时给多个变量赋值
# x,y,z = 1,2,3
# print(x,y,z)

# ##常量
# MAX_CONNECTIONS = 5000
# print(MAX_CONNECTIONS)			##将变量名全部大写 用来表示常量


import this							##Python之禅



















