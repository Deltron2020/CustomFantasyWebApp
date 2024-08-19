from flask import Blueprint, render_template, request, flash
from FA_Authorize.sql import insert_user_sql

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template('FA_Login.html')

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        flash('Sign Up Successful!', category='success')
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password')
        password2 = request.form.get('confirm')
        dob = request.form.get('dob')
        promo = request.form.get('promo')

        #print(request.form)
        insert_user_sql(username, email, password1, dob, promo)

    return render_template('old/old/FA_Signup.html')
