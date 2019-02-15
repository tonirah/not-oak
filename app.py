import os
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

from label import label_leaf

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = './pictures'

app = Flask(__name__)
app.secret_key = '@3xffxbex9b5x06:x8f=xc0x04x15Bxe6xc2'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

cloudinary.config( 
  cloud_name = "toni-not-oak", 
  api_key = "866339269462168", 
  api_secret = "TwmBPqSIbsuwWcG2w3-SrkokM2Q" 
)


@app.route('/')
def index():
  leaf_result = label_leaf("leaves/leaves_examples/toni_n_0.jpg")
  return render_template("index.html", leaf=leaf_result['labels'][0],
                         certainty=leaf_result['results'][0], 
                         time=leaf_result['time'])


@app.route('/cloud', methods=['GET', 'POST'])
def upload_file():
    upload_result = None
    thumbnail_for_model = None
    thumbnail_for_user = None
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file_to_upload = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file_to_upload.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # Check if filetype is okay
        if not allowed_file(file_to_upload.filename):
            flash('File-type not allowed. Use .png, .jpg or .jpeg.')
            print('File-type not allowed. Use .png, .jpg or .jpeg.')
            return redirect(request.url)
        # Upload file
        upload_result = upload(file_to_upload, folder = 'uploads')
        thumbnail_for_model, options = cloudinary_url(upload_result['public_id'], format="jpg", crop="fill", width=299,
                                                 height=299)
        thumbnail_for_user, options = cloudinary_url(upload_result['public_id'], format="jpg", crop="fit", width=600,
                                                 height=600)

    return render_template('upload_form.html', upload_result=upload_result, thumbnail_for_model=thumbnail_for_model,
thumbnail_for_user=thumbnail_for_user)




def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS