from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Welcome to Raspberry Pi'
    return app.send_static_file('index.html')