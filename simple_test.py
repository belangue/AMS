# simple_test.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    print("Route accessed!")
    return "Hello, World!"

if __name__ == '__main__':
    print("Starting Flask application...")
    app.run(debug=True)