
result = parse.delay()
print result.ready()

with open('home/ubuntu/testt.txt', 'w+') as f:
	f.write(str(result.ready()))

while result.ready() == False:
	k = 1

with open('home/ubuntu/test.txt', 'w+') as f:
	f.write(result)