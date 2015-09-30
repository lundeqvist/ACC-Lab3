import os
import json

pronouns = {"han":0, "hon":0, "den":0, "det":0, "denna":0, "denne":0, "hen":0}

with open('tweets_19.txt', 'r') as f:
	for l in f:
		try:
			if json.loads(l)["retweeted"] == False:
				tweet = json.loads(l)["text"].split()
				for p in pronouns.keys():
					if p in tweet:
						pronouns[p] += 1
		except:
			pass
print pronouns