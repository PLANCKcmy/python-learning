
with open('C:\\Users\\94216\\Desktop\\to\\hhh.py','r') as files:
	context=files.read()
	with open('C:\\Users\\94216\\Desktop\\to\\happy.txt','w') as files2:
		files2.write(context)
		files2.close
	files.close
with open('C:\\Users\\94216\\Desktop\\to\\happy.txt','r') as files3:
	print(files3.read())


