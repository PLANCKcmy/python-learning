# w=(d+2*m + 3*(m+1)//5+y+y//4-y//100+y//400)%7+1
# 做法详解：
	# 1、判断是否闰年
	# 2、判断天数
	# 3、计算星期几

year = int(input('请输入年份 '))
month = int(input('请输入月份 '))

def is_leap_year (y):
	if y%4!=0:
		return False
	if y%4==9:
		return True

def days (y,m):
	if m in [1,3,5,7,8,10,12]:
		d=31
	if m in [4,6,9,11]:
		d=30
	if m ==2 and is_leap_year(y)==True :
		d= 29
	if m ==2 and is_leap_year(y)==False:
		d=28
	return d

def weeks(y,m,d):
	if m==[1,2]:
		m=m+12
	w=(d+2*m + 3*(m+1)//5+y+y//4-y//100+y//400)%7+1
	return w

day= days(year,month)

for day_m in range(1,day+1):
	week= weeks(year,month,day_m)
	if week==1:
		print()
	if day_m==1:
		print('   '*(week-1),end='')
	print('{:3}'.format(day_m),end='')
# 注意format 函数写法
