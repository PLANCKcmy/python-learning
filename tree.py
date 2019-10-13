def is_end(i,s):
	if i == 0:
		print('游戏结束，你甚至还没有玩耍')
	if i == 1 and s not in [0,-1]:
		print('游戏结束，恭喜你赢得')
	if i == 1 and s == 0:
		final ='游戏结束，你一分都没有'
		return final
	if i == 1 and s == -1:
		print ('游戏正式开始')
		return True
	if i not in [0,1]:
		print ('您输入的值不符合规范请从新输入')
		return False

is_end(1,50)