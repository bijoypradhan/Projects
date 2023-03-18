from flask import render_template, request, session, redirect, url_for

from langapp_files import app, db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(150), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return '<Email %r>' % self.email

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if session['loggedin'] == True:
        return render_template('home.html')
    return render_template(
            'index.html', session=session
        )

# @app.route('/home')
# def home():
#     return render_template(
#             'home.html'
#         )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        # account = Users.query.filter(Users.email == email)
        # check = Users.query.all()
        # check1 = Users.query.filter.get_or_404(email)
        # print(check1)
        account = Users.query.filter_by(email=email).first()
        if account:
            session['loggedin'] = True
            session['email'] = email
            return render_template('home.html')
    return render_template(
            'login.html'
        )


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session['loggedin'] = False
   return redirect(url_for('index'))


@app.route('/register')
def register():
    return render_template(
            'register.html'
        )

