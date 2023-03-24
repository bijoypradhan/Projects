from flask import Blueprint, render_template, request, session, redirect, url_for

from .models import Users

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        account = Users.query.filter_by(email=email).first()
        if account:
            session['loggedin'] = True
            session['email'] = email
            return render_template('home.html')
    return render_template(
            'login.html'
        )

@auth.route('/logout')
def logout():
   # remove the username from the session if it is there
   session['loggedin'] = False
   return redirect(url_for('views.index'))


@auth.route('/register')
def register():
    return render_template(
            'register.html'
        )