import os
from tasks import parse
from flask import Flask, jsonify
import matplotlib.pyplot as pyplot

app = Flask(__name__)

@app.route('/pronouns', methods=['GET'])
def parse_pronouns():
	result = parse.delay()
	while result.ready() == False:
		k = 1

	pronouns = result.get()

	x_keys = pronouns.keys()
	y_values =  pronouns.values()
	total_values = float(sum(y_values))
	x = [1,2,3,4,5,6,7]
	y = [v / total_values for v in y_values]
	pyplot.title('Pronouns')
	pyplot.bar(x, y, align='center', width=0.65)
	pyplot.xticks(x, x_keys)
	pyplot.savefig('pronouns.png')

	return jsonify(pronouns),200

@app.route('/celery', methods=['GET'])
	c.delay(5)
	c.delay(25)

@app.route('/', methods=['GET'])
def test():
	return "Foo"

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)

