import os
from remote import parse
from celery import group

def app():
	baseurl = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/'
	tweets_files = ['tweets_0.txt', 'tweets_1.txt', 'tweets_2.txt', 'tweets_3.txt', 'tweets_4.txt', 'tweets_5.txt', 'tweets_6.txt', 'tweets_7.txt']
	
	tasks = []
    for tweets in tweets_files:
        tasks.append(parse.delay(tweets))
    get = [t.get() for t in tasks]
    return get