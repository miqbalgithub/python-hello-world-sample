from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"
    
@app.route('/1')
def hello1():
    return "Halaman 1"
    
@app.route('/2')
def hello2():
    return "Halaman 2"

@app.route3('/3')
def hello():
    return "Halaman 3"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')