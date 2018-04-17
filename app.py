from flask import Flask
app = Flask(__name__)

from label import label_leaf

@app.route('/')
def hello_world():
  return label_leaf("leaves/leaves_examples/eiche0.jpeg")