

from controller.attendanceController import *

from flask import Blueprint

# Define your sub-app logic in a separate file (e.g., sub_app.py)
result = Blueprint('result', __name__)


@result.route('/')
def hello_world():
    name = "John"
    return render_template('test.html', name=name)
    # return "Hello, World Welcome to the result app! ResultApp"

