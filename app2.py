import os
from remote import parse
from celery import group

def app():
	baseurl = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/'
	tweets_files = ['tweets_0.txt', 'tweets_1.txt', 'tweets_2.txt', 'tweets_3.txt', 'tweets_4.txt', 'tweets_5.txt', 'tweets_6.txt', 'tweets_7.txt']
	parser_jobs = group(parse(baseurl + url) for t_file in tweets_files)
	result = parser_jobs.apply_async()
	print str(result.ready())
	while result.ready() == False:
		k = 1

	print str(result.get())