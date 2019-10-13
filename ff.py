# w=(d+2*m + 3*(m+1)//5+y+y//4-y//100+y//400)%7+1
m_31=(13,3,5,7,8,10,12)
m_30=(4,6,9,11)

y=int(input('请输入年份'))
m=int(input('请输入月份'))
if m==1 or m==2:
	m=m+12
	y=y-1
if m in m_30:
	d=30
if m in m_31:
	d=31
if y%4==0 and m==14:
	d=29
if y%4 !=0 and m==14:
	d=28
def w(y,m):
	w=(d+2*m + 3*(m+1)//5+y+y//4-y//100+y//400)%7+1
	return w

print ('一  二  三  四  五  六  日')
print ('—'*20)

for d in range(1,d+1):
	s=w(y,m)
	if d==1 and s!=1:
		print (' '*2*s,d,end='   ')
	if d>=2 and d<=9:
		if s==7:
			print (d)
		if s!=7:
			print (d,end='   ')
	if d>9:
		if s==7:
			print (d)
		if s!=7:
			print (d,end='  ')


