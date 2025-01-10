from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Handle login logic here
        return redirect(url_for('attendance'))  # Redirect to a dashboard or home page
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        dob = request.form['dob']
        password = request.form['password']
        # Handle registration logic here
        return redirect(url_for('login'))  # Redirect to the login page
    return render_template('signup.html')


