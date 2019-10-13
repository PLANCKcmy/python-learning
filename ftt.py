# 1、比大小的函数
print ('please guess what i have written before')
import random
num=random.randint(1,100)
# 注意随机数的生成方法，import 

def is_equal (n,a):
	if n!=a:
		if n< a:
			print ('too big')
		else :
			print('too small')
		return False
	if n==a:
		print ('yes you are right and the answer is ', n)
		return True

s= False
while s==False:
	answer = int(input('the answer is '))
# is_equal(num,answer)
# 注意给函数一个承接值，相当于运行函数
	s= is_equal(num,answer)
	# 注意，什么是应该在循环里面的，什么是应该在循环外面的


