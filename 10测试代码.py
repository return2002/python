# '''
# name_funcation.py:

# def get_formatted_name(first,last):
# 	full_name = f"{first} {last}"
# 	return full_name.title()
# '''
# #测试函数
# from name_funcation import get_formatted_name
# print("Enter 'q' at any time to quit.")
# while True:
# 	first = input("first name:")
# 	if first == 'q':
# 		break
# 	last = input("last name:")
# 	if last == 'q':
# 		break

# 	formatted_name = get_formatted_name(first,last)
# 	print(f"\tNeatly formatted name: {formatted_name}")






# ##如上 代码可正确执行 但是当对get_formatted_name()进行修改时 每次都要运行这个python文件 并输入参数进行测试 十分繁琐
# ##python提供了一种自动测试函数输出的高效方式
# #单元测试和测试用例

# #可通过的测试
# ##引入unittest模块 和测试函数
# import unittest
# from name_funcation import get_formatted_name

# #创建一个类 继承unittest.TestCase类
# class NamesTestCase(unittest.TestCase):
# 	def test_frist_last_name(self):
# 		fromatted_name = get_formatted_name('janis','joplin')
# 		self.assertEqual(fromatted_name,'Janis Joplin')					##断言方法 判断期望fromatted的值 是否与期望结果一致

# if __name__ == '__main__':												##如果这个文件被测试框架导入 __name__的值将不是__main__就不会执行这个代码
# 	unittest.main()





# '''
# 修改name_funcation.py:

# def get_formatted_name(first, middle, last):
# 	"""生成整洁的姓名。"""
# 	full_name = f"{first} {middle} {last}"
# 	return full_name.title())
# '''
# ##未通过测试
# ##引入unittest模块 和测试函数
# import unittest
# from name_funcation import get_formatted_name

# #创建一个类 继承unittest.TestCase类
# class NamesTestCase(unittest.TestCase):
# 	def test_frist_last_name(self):
# 		fromatted_name = get_formatted_name('janis','joplin')
# 		self.assertEqual(fromatted_name,'Janis Joplin')					##断言方法 判断期望fromatted的值 是否与期望结果一致

# if __name__ == '__main__':												##如果这个文件被测试框架导入 __name__的值将不是__main__就不会执行这个代码
# 	unittest.main()

#报错信息 解释：
'''
E    																		##'E'说明测试用例中有一个单元测试导致了错误
======================================================================
ERROR: test_frist_last_name (__main__.NamesTestCase)						##指出哪个单元引发的错误
----------------------------------------------------------------------
Traceback (most recent call last):
  File "../10测试代码.py", line 65, in test_frist_last_name					##指出具体哪一行有问题
    fromatted_name = get_formatted_name('janis','joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

----------------------------------------------------------------------
Ran 1 test in 0.001s														##运行了一个单元测试

FAILED (errors=1)															##测试该用例时发誓一个错误
'''







# ##然后根据提示信息进行被测试代码
# '''
# def get_formatted_name(first, last, middle=''):
# 	"""生成整洁的姓名。"""
# 	if middle:
# 		full_name = f"{first} {middle} {last}"
# 	else:
# 		full_name = f"{first} {last}"
# 	return full_name.title()
# '''
# import unittest
# from name_funcation import get_formatted_name

# #创建一个类 继承unittest.TestCase类
# class NamesTestCase(unittest.TestCase):
# 	def test_frist_last_name(self):
# 		fromatted_name = get_formatted_name('janis','joplin')
# 		self.assertEqual(fromatted_name,'Janis Joplin')					##断言方法 判断期望fromatted的值 是否与期望结果一致

# if __name__ == '__main__':												##如果这个文件被测试框架导入 __name__的值将不是__main__就不会执行这个代码
# 	unittest.main()






# ##添加新测试
# import unittest
# from name_funcation import get_formatted_name

# #创建一个类 继承unittest.TestCase类
# class NamesTestCase(unittest.TestCase):
# 	def test_frist_last_name(self):
# 		fromatted_name = get_formatted_name('janis','joplin')
# 		self.assertEqual(fromatted_name,'Janis Joplin')					##断言方法 判断期望fromatted的值 是否与期望结果一致

# 	def test_first_last_middle_name(self):
# 		"""能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
# 		formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
# 		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

# if __name__ == '__main__':												##如果这个文件被测试框架导入 __name__的值将不是__main__就不会执行这个代码
# 	unittest.main()










#测试类
#各种断言方法
'''
------------------------------------------------------------
	方法 							用途
------------------------------------------------------------
assertEqual(a, b) 				核实a == b
assertNotEqual(a, b) 			核实a != b
assertTrue(x) 					核实x 为True
assertFalse(x) 					核实x 为False
assertIn(item , list ) 			核实 item 在 list 中
assertNotIn(item , list ) 		核实 item 不在 list 中
------------------------------------------------------------
'''


#一个要测试的类
'''
survey.py :

class AnonymousSurvey:
	"""收集匿名调查问卷的答案。"""
	def __init__(self, question):
		"""存储一个问题，并为存储答案做准备。"""
		self.question = question
		self.responses = []
	def show_question(self):
		"""显示调查问卷。"""
		print(self.question)
	def store_response(self, new_response):
		"""存储单份调查答卷。"""
		self.responses.append(new_response)
	def show_results(self):
		"""显示收集到的所有答卷。"""
		print("Survey results:")
		for response in self.responses:
			print(f"- {response}")

'''

# ##证明survery.py能正常运行
# from survey import AnonymousSurvey
# # 定义一个问题，并创建一个调查。
# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)
# # 显示问题并存储答案。
# my_survey.show_question()
# print("Enter 'q' at any time to quit.\n")
# while True:
# 	response = input("Language: ")
# 	if response == 'q':
# 		break
# 	my_survey.store_response(response)
# # 显示调查结果。
# print("\nThank you to everyone who participated in the survey!")
# my_survey.show_results()


# #注释掉上边这段
# #测试AnonymousSurvey类
# import unittest
# from survey import AnonymousSurvey
# class TestAnonymousSurvey(unittest.TestCase):
# 	"""针对AnonymousSurvey类的测试。"""
# 	def test_store_single_response(self):
# 		"""测试单个答案会被妥善地存储。"""
# 		question = "What language did you first learn to speak?"
# 		my_survey = AnonymousSurvey(question)
# 		my_survey.store_response('English')
# 		self.assertIn('English', my_survey.responses)					##断言方法assertIn() 上边有对应功能的表格

# 	##下面来核实当用户提供三个答案时，它们也将被妥善地存储
# 	def test_store_three_responses(self):
# 		"""测试三个答案会被妥善地存储。"""
# 		question = "What language did you first learn to speak?"
# 		my_survey = AnonymousSurvey(question)
# 		responses = ['English', 'Spanish', 'Mandarin']
# 		for response in responses:
# 			my_survey.store_response(response)
# 		for response in responses:
# 			self.assertIn(response, my_survey.responses)

# if __name__ == '__main__':
# 	unittest.main()






#方法setUp()
import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
	"""针对AnonymousSurvey类的测试。"""
	def setUp(self):											#如果测试类包含setUp() 只需要创建对象一次 python先运行它 再运行各个以test_打头的方法  测试方法中都可以使用setUo()中创建的对象
	# 创建一个调查对象和一组答案，供使用的测试方法使用。
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English', 'Spanish', 'Mandarin']
	def test_store_single_response(self):
		"""测试单个答案会被妥善地存储。"""
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)
	def test_store_three_responses(self):
		"""测试三个答案会被妥善地存储。"""
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
	unittest.main()
