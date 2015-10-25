import os
import sys
import urllib2, json
import glob
from celery import Celery



app = Celery('tasks2', backend='amqp', broker='amqp://elias:pass@' + os.environ['master_ip'] + ':5672/geijer')

@app.task
def parse2(url):
	data = urllib2.urlopen(url)
	pronouns = {"han":0, "hon":0, "den":0, "det":0, "denna":0, "denne":0, "hen":0}
	n = 0
	for line in data:
		try:
			tweet = json.loads(line)
			if 'retweeted_status' not in tweet:
				tweet_text = tweet["text"].lower()
				words = tweet_text.split()
				for p in pronouns.keys():
					if p in words:
						n += 1
						pronouns[p] += 1
		except:
			pass
			
	pronouns.update({'n_tweets': n})
	return pronouns