import os
import json
import glob
from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://elias:pass@130.238.29.126:5672/geijer')

@app.task
def c(x):
	return str(x*x*x)