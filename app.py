from flask import Flask, render_template, Response, request, redirect
import os
from main import generate_frame
from ParkingSpacePicker import parkingspacepicker

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/detection', methods = ['GET', 'POST'])
def detection():
	if request.method == "POST":
		if 'upload' not in request.files:
			print("no file part")
			return redirect("/")
		file = request.files['upload']
		if file.filename == '':
			print('No image selected for uploading')
			return redirect(request.url)
		else:
			# base_path = os.path.abspath(os.path.dirname(__file__))
			# print(base_path)
			# upload_path = os.path.join(base_path, "video")
			# print(upload_path)
			# f.save(os.path.join(upload_path, secure_filename(f.filename)))
			# filename = secure_filename(file.filename)
			filename = "output.mp4"
			print(filename)
			file.save(os.path.join("output video", filename))
			# print('upload_video filename: ' + filename)
			print("successful")
			# flash('Video successfully uploaded and displayed below')
			return render_template('detection.html', filename=filename)
	return render_template('detection.html')

@app.route('/anotation')
def anotation():
	# display = 0
	return render_template('anotation.html')

@app.route('/video/<filename>')
def video(filename):
	print('display_video filename: ' + filename)
	display = filename
	return Response(generate_frame(display),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/videocam')
def videocam():
	display = 0
	return Response(parkingspacepicker(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)

