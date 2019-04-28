import os
from flask import Flask, render_template, request
from ocr_core import ocr_core

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

# function to check the file extension
def allowed_file(filename):
	return "." in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the homepage
@app.route('/')
def home_page():
	return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
	if request.method == 'POST':
		if 'file' not in request.files:
			return render_template('upload.html', msg='No file selected')
		
		file = request.files['file']

		if file.filename == '':
			return render_template('upload.html', msg='No file selected')

		if file and allowed_file(file.filename):
			extracted_text = ocr_core(file)
			print('{}'.format(file.filename))
			return render_template(
				'upload.html', 
				msg='Successfully processed', 
				extracted_text=extracted_text,
				img_src=UPLOAD_FOLDER + file.filename
			)
	elif request.method == 'GET':
		return render_template('upload.html')

@app.route('/hello/<int:score>')
def hello_name(score):
	return render_template('hello.html', record=score)

dict = {'Physics':50, 'Math':60, 'Chemistry':100}

@app.route('/result')
def result():
	return render_template('result.html', result = dict)

if __name__ == '__main__':
	app.run()