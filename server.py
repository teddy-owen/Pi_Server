from flask import Flask
import subprocess 
app = Flask(__name__)


@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/cam')
def toggle_camera():
	camera_off = subprocess.call(["systemctl", "is-active", "--quiet", "stream-cam.service"])
	if camera_off:
		subprocess.call(["systemctl", "start", "stream-cam.service"])
		return "Camera on"
	else:
		subprocess.call(["systemctl", "stop", "stream-cam.service"])
		return "Camera off"