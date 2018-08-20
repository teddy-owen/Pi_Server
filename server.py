from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/cam')
def toggle_camera():
	print('Cam route')
    return "Camera on"