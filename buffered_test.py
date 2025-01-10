from flask import Flask
import sys
import os

os.environ['PYTHONUNBUFFERED'] = '1'

app = Flask(__name__)

@app.route('/')
def hello():
    sys.stdout.write("Route accessed!\n")
    sys.stdout.flush()
    return "Hello, World!"

if __name__ == '__main__':
    sys.stdout.write("Starting Flask application...\n")
    sys.stdout.flush()
    app.run(debug=True)