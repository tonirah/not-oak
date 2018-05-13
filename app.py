from flask import Flask, render_template
app = Flask(__name__)

from label import label_leaf

@app.route('/')
def index():
  leaf_result = label_leaf("leaves/leaves_examples/eiche0.jpeg")
  return render_template("index.html", leaf=leaf_result['labels'][0],
  											 certainty=leaf_result['results'][0], 
  											 time=leaf_result['time'])