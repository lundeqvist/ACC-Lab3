import os
from tasks import parse
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/pronouns', methods=['GET'])
def parse_pronouns():
	result = parse.delay()
	while result.ready() == False:
		k = 1
	#data = subprocess.check_output(result.get())
	return jsonify(result.get()),200

if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)