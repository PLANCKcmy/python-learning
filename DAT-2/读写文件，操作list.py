with open('score_practise.txt','w') as file:
	data='刘备 90 89 67\n善战 56 45\n十米 34 22 33 66\n'
	file.write(data)
file.close
#编辑一个文件
with open('score_practise.txt','r') as file:
	lines=file.readlines()
	#print(lines)
	#内容转成一个列表
	for line in lines:
		#print(line)
		#遍历列表,现在每行都是字符串
		data=line.split(' ')
		data.insert(1,':')
		#每行根据空格将字符串组合成列表
		data1=' '.join(data)
		#print(data,type(data))
		sum = 0
		for score in data[2:]:
			#遍历列表中的除了头部以外的位置
			sum=sum+int(score)
		score_context=data1+'求和='+str(sum)+'\n'
		#编辑成想要的样子
		#print(score_sum)
		with open('score_practise.txt','a') as sumfile:
			sumfile.write(score_context)
			#只能写字符串
