# API
from flask import *
import json, time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  data_set = { 'Page': 'Home', 'MSG': 'deu bom', 'time': time.time()}
  json_dump = json.dumps(data_set)

  return json_dump

app.run(host='0.0.0.0')


#host='0.0.0.0'  