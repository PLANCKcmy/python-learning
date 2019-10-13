l=[]
for i in range(100,1001):
	a=i%10
	b=i//10%10
	c=i//100%10
	import math
	if a**3+b**3+c**3==100*c+b*10+a:
		l.append(i)
print(l[0])

#找出100以内所有质数
m=[]
for i in range(1,101):
	l=[j for j in range(1,i+1) if i%j==0]
	if len(l)==2:
		m.append(i)
print(m)

#打印九九乘法表

l=[[
	'{:1}'.format(i),
	'{:1}'.format('*'),
	'{:1}'.format(j), 
	'{:1}'.format('='),
	'{:2}'.format(i*j),
	for j in range(1,10)] for i in range (1,10)]
print(l)
