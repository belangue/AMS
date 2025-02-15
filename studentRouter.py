from controller.studentController import *

from flask import Blueprint,render_template

# Define your sub-app logic in a separate file (e.g., sub_app.py)
student = Blueprint('student', __name__)

# @student.route('/')
# def hello_world():
#     return "Hello, World Welcome to the result app! ResultApp"

@student.route('/')
def hello_world():
    name = "John"
    return render_template('test.html', name=name)


@student.route("/getAllStudent", methods=['GET'])
def getStudent():
    pass


@student.route("/createStudent", methods=['POST'])
def createStudent():
    pass


@student.route("/updateStudent/<matricule>", methods=['PUT'])
def updateStudent(matricule):
    pass


@student.route("/deleteStudent/<matricule>", methods=['DELETE'])
def deleteStudent(matricule):
    pass