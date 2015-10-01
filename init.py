import os
from tasks import parse


result = parse.delay()
print result.ready()

with open('testt.txt', 'w+') as f:
	f.write(str(result.ready()))

while result.ready() == False:
	k = 1

with open('test.txt', 'w+') as f:
	f.write(result)
m = 1