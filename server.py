from flask import Flask
import subprocess 
app = Flask(__name__)

CAMERA_ON = False

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/cam')
def toggle_camera():
	if not CAMERA_ON:
		subprocess.call(["systemctl", "start", "stream-cam.service"])
		CAMERA_ON = True
		return "Camera on"
	else:
		subprocess.call(["systemctl", "stop", "stream-cam.service"])
		CAMERA_ON = False
		return "Camera off"