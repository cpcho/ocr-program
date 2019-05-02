import os
from flask import Flask, render_template, request, url_for 
# from werkzeug.utils import secure_filename
from ocr_core import ocr_core

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
	if request.method == 'POST':
		# check if the post request has the file part
		if 'file' not in request.files:
			# flash('No file part')
			return render_template('upload.html', msg='No file selected')
		file = request.files['file']
		# if user does not select file, browser also
        # submit an empty part without filename
		if file.filename == '':
			return render_template('upload.html', msg='No file selected')
		if file and allowed_file(file.filename):
			extracted_text = ocr_core(file)
			# filename = secure_filename(file.filename)
			filename = file.filename
			# file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return render_template(
				'upload.html',
				msg='Successfully processed', 
				extracted_text=extracted_text,
				img_src=UPLOAD_FOLDER + filename,
				# img_src=os.path.join(app.config['UPLOAD_FOLDER'],filename)
			)
	elif request.method == 'GET':
		return render_template('upload.html')

@app.route('/student')
def student():
	return render_template('student.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		return render_template('result.html', result=result)

# route and function to handle the homepage
# @app.route('/')
# def home_page():
# 	return render_template('index.html')
# @app.route('/hello/<int:score>')
# def hello_name(score):
# 	return render_template('hello.html', record=score)

if __name__ == '__main__':
	app.run()