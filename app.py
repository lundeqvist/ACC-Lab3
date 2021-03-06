import os, subprocess, celery, time
from celery import group
from tasks1 import parse1
from tasks2 import parse2
from flask import Flask, jsonify
from collections import Counter
#import matplotlib.pyplot as pyplot

app = Flask(__name__)

@app.route('/pronouns1', methods=['GET'])
def parse_pronouns1():
	result = parse1.delay()
	while result.ready() == False:
		k = 1

	pronouns = result.get()

	x_keys = pronouns.keys()
	y_values =  pronouns.values()
	total_values = float(sum(y_values))
	x = [1,2,3,4,5,6,7]
	y = [v / total_values for v in y_values]

	'''
	Add the following line to userdata-broker.yml:
	- pip install matplotlib
	and install pkg-config in order to plot it from 
	the broker
	'''

	#pyplot.title('Pronouns')
	#pyplot.bar(x, y, align='center', width=0.65)
	#pyplot.xticks(x, x_keys)
	#pyplot.savefig('pronouns.png')

	return jsonify(pronouns),200


@app.route('/pronouns2/<int:n_files>', methods=['GET'])
def parse_pronouns2(n_files):
	if n_files > 0 and n_files < 21:
		baseurl = 'http://smog.uppmax.uu.se:8080/swift/v1/tweets/'
		tweets_files = ['tweets_0.txt', 'tweets_1.txt', 'tweets_2.txt', 'tweets_3.txt', 'tweets_4.txt', 
						'tweets_5.txt', 'tweets_6.txt', 'tweets_7.txt', 'tweets_8.txt', 'tweets_9.txt', 
						'tweets_10.txt', 'tweets_11.txt', 'tweets_12.txt', 'tweets_13.txt', 'tweets_14.txt', 
						'tweets_15.txt', 'tweets_16.txt', 'tweets_17.txt', 'tweets_18.txt', 'tweets_19.txt']
		
		job = group([parse2.s(baseurl + tweets) for tweets in tweets_files[0:n_files]])
		before = time.time()
		result = job.apply_async()
		
		while result.ready() == False:
			k = 1

		answers = result.get()
		elapsed_time = time.time() - before
		pronouns = Counter({})
		for t in answers:
			pronouns.update(t)
		pronouns.update({'time_taken': elapsed_time})
		return jsonify(dict(pronouns)),200
	else:
		return "Not valid amount of tweets"

@app.route('/', methods=['GET'])
def test():
	return "Foo"

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)

