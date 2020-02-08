from flask import Flask, render_template, url_for, flash, redirect, session,request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def articles():
    return render_template('blog.html')

@app.route('/blog/<string:id/>')
def blog(id):
    return render_template('blog-single.html')

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=2, max=35)])
    email = StringField('Email', [validators.Length(min=6, max=55)])
    password = PasswordField('Password', [validators.DataRequired(),
    validators.EqualTo('confirm', message = 'Passwords do not match')
    ])
    confirm = PasswordField('Confirm password')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html', form = form)


if __name__ == '__main__':
    app.run(debug=True)

