import os
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = './pictures'

app = Flask(__name__)
app.secret_key = '@3xffxbex9b5x06:x8f=xc0x04x15Bxe6xc2'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from label import label_leaf

@app.route('/')
def index():
  leaf_result = label_leaf("leaves/leaves_examples/toni_n_0.jpg")
  return render_template("index.html", leaf=leaf_result['labels'][0],
                         certainty=leaf_result['results'][0], 
                         time=leaf_result['time'])


@app.route('/upload', methods=['GET', 'POST'])
def upload():
  if request.method == 'POST':
      # Check if the post request has the file part
      if 'file' not in request.files:
          flash('No file part')
          print('No file part')
          return redirect(request.url)
      file = request.files['file']
      # If user does not select file, browser also
      # submit an empty part without filename
      if file.filename == '':
          flash('No selected file')
          print('No selected file')
          return redirect(request.url)
      # Check if filetype is okay
      if not allowed_file(file.filename):
          flash('File-type not allowed. Use .png, .jpg or .jpeg.')
          print('File-type not allowed. Use .png, .jpg or .jpeg.')
          return redirect(request.url)
      # Save file
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return redirect(url_for('uploaded_file', filename=filename))
  return render_template("upload.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
  return send_from_directory(app.config['UPLOAD_FOLDER'],
                             filename)


def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS