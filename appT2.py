import os, subprocess
from remote import parse
from celery import group
from collections import Counter

def app():
	baseurl = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/'
	tweets_files = ['tweets_0.txt', 'tweets_1.txt', 'tweets_2.txt', 'tweets_3.txt', 'tweets_4.txt', 'tweets_5.txt', 'tweets_6.txt', 'tweets_7.txt', 'tweets_8.txt', 'tweets_9.txt', 'tweets_10.txt', 'tweets_11.txt', 'tweets_12.txt', 'tweets_13.txt', 'tweets_14.txt', 'tweets_18.txt', 'tweets_19.txt']
	
	job = group([parse.s(baseurl + tweets) for tweets in tweets_files])
	result = job.apply_async()

	while result.ready() == False:
		k = 1

	answers = result.get()

	p = Counter({})
	for t in answers:
		p.update(t)

	return dict(p)