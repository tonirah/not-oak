from flask import Flask, render_template
app = Flask(__name__)

from label import label_leaf

@app.route('/')
def index():
  output = label_leaf("leaves/leaves_examples/eiche0.jpeg")
  return render_template("index.html", output=output)