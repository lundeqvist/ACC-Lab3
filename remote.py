import os
import sys
import urllib2, json
import glob
from celery import Celery



app = Celery('tasks', backend='amqp', broker='amqp://elias:pass@130.238.29.14:5672/geijer')

@app.task
def parse(url):
	data = urllib2.urlopen(url)
	pronouns = {"han":0, "hon":0, "den":0, "det":0, "denna":0, "denne":0, "hen":0}
	for line in data:
		try:
			if json.loads(line)["retweeted"] == False:
				tweet = json.loads(line)["text"].split()
				for p in pronouns.keys():
					if p in tweet:
						pronouns[p] += 1
		except:
			pass
	return pronouns