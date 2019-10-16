#比大小
#比赛结果
#控制游戏开始（用函数来表达）
#判断游戏开始
#判断游戏难度

'''1、判断游戏开始：'''

def is_begin(s):
	if s == 0:
		return False
	if s == 1:
		return True

'''2、判断大小'''
def is_equal(a,n):
	if a == n:
		print('yes,you are right!')
		return True
	if a > n:
		print('too big')
		return False
	if a < n:
		print('too small')
		return False

'''3、判断游戏结局'''
def is_ending(t,s):
	if t == 0 and s==0:
		ending='sorry,you earn no score '
		return ending
	if s != 0:
		ending = f'congratulations! you have {t},and you earn {s} '
		return ending
	if t != 0 and s == 0:
		ending = f'you have {t} times,try again please'
		return ending

def game(a):
	#import random
	#num=random.randint(1,100)
	num=50
	print('choose model : 0：简单 1：普通 2：困难 3：地域')
	model=int(input())
	times=10-model
	print(f'now you have {times}times')
	for time in range(times-1,-1,-1):
		answer=int(input('answer='))
		s=is_equal(answer,num)
		if s== False:
			print(is_ending(time,0))
		if s== True:
			score= 100-10*(10-time)+10*(1+model)
			print(is_ending(time,score))
			break
	print(f'the right answer is {num}')
	return time,score

print('what you name?')
name=input()
print('choose to begin game or not?')
begin=int(input('0 or 1 \n'))
if is_begin(begin)== True:
	dataname=game(0)
	nowtime=10-float(dataname[0])
	nowscore=float(dataname[1])
	print(nowtime,nowscore)
#开始游戏承接函数

with open('gameguess.txt','r') as file1:
	lines=file1.readlines()
	file1.close

scores={}
for line in lines:
	data=line.split(' ')
	scores[data[0]]=data[1:]
	#将现有的成绩添加进去，名字是key，后面的是value

score=scores.get(name)
if score==None:
	score=[0,0,0]
	#确认是否有成绩，如果没有就重新生成一个

avergetime=score[0]
avergescore=score[1]
playtimes=score[2]
#找到已有成绩

playtimes=int(playtimes)+1
avergetime=(float(avergetime)*(playtimes-1)+float(nowtime))/playtimes
avergescore=(float(avergescore)*(playtimes-1)+float(nowscore))/playtimes
playtimes=str(playtimes)
avergescore=str(avergescore)
avergetime=str(avergetime)
#计算成绩,并转化函数

score=[avergetime,avergescore,playtimes]
scores[name]=score
read=''
for i in scores:
	score=' '.join(scores[i])
	line=f'{i} {score}'
	read=read+line
#将过去的数据一同存储

with open('gameguess.txt','w+') as file:
	file.write(read)
	file.close

print(f'name:{name}\nnowtime:{nowtime}\nnowscore:{nowscore}\navergetime:{avergetime}\navergescore:{avergescore}\nplaytimes:{playtimes}')

with open('gameguess.txt','r') as file:
	print(file.read())
	file.close
