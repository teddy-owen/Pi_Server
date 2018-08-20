from flask import Flask
app = Flask(__name__,static_url_path='/home/teddy/Documents/Pi_Server/static')

@app.route('/')
def hello_world():
    # return 'Welcome to Raspberry Pi'
    return app.send_static_file('index.html')