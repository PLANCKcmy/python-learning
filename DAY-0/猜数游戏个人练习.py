

def is_end(i,s):
	if i == 0:
		print('游戏结束，你甚至还没有玩耍')
	if i == 1 and s not in [0,-1]:
		final ='游戏结束，恭喜你赢得{}'.format(s)
		return final
	if i == 1 and s == 0:
		final ='游戏结束，你一分都没有'
		return final
	if i == 1 and s == -1:
		print ('游戏正式开始')
		return True
	if i not in [0,1]:
		print ('您输入的值不符合规范请从新输入')
		return False

def is_equal(n,a):
	if n<a:
		x= '太大,'
		return x
	if n>a:
		x= '太小,'
		return x
	if n==a:
		x= '呦对了,'
		return x

def game(g):
	import random
	num = random.randint(1,100)
	print ('请选择难度：简单：0，普通：1，困难：2')
	model = int(input())
	times = 7-model
	score=0
	print ('您一共有 ',times,'次机会')
	for time in range(times,0,-1):
		answer = int(input('你猜的数是 '))
		sur = is_equal(num,answer)
		if time-1 != 0 and sur!='呦对了,':
			s = sur+'您还有 '+str(time-1)+' 次机会'
			print (s)
		if time-1 != 0 and sur =='呦对了,':
			score=score+time*10
			s = is_end(1,score)
			print (s)
			break
		if time-1 == 0 and sur!='呦对了,':
			s = is_end(1,0)
			print (s)
			break
		if time-1 == 0 and sur=='呦对了,':
			s = is_end(1,score)
			print (s)
			break

print('请您确认是否开始游戏\n','开始请按1\n','取消请按0')

go_on = 0
end = False
score = -1

while end == False:
	go_on = int(input())
	end = is_end(go_on,score)
if  end == True:
    game(1)
    
