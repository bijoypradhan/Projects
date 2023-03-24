from flask import Blueprint, render_template, request, session, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/index', methods=['GET', 'POST'])
def index():
    try:
        session['loggedin']
    except:
        session['loggedin'] = False
    if session['loggedin'] == True:
        return render_template('home.html')
    return render_template(
            'index.html', session=session
        )



