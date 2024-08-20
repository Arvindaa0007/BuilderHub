from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from db_conn import db_connect
from werkzeug.security import check_password_hash

login_bp = Blueprint('login', __name__)

@login_bp.route('/process_login', methods=['GET', 'POST'])
def process_login():
    if request.method == 'POST':
        email_id = request.form['username']
        password = request.form['password']

        connection = None
        cursor = None

        try:
            connection = db_connect()
            cursor = connection.cursor(dictionary=True)

            query = "SELECT * FROM User WHERE email_id = %s"
            cursor.execute(query, (email_id,))
            user = cursor.fetchone()

            if user and check_password_hash(user['password'], password):
                session['email_id'] = email_id
                flash('Login successful!')
                return redirect(url_for('dashboard.dashboard'))
            else:
                flash('Invalid email or password!')
                return redirect(url_for('login.login'))
        except Error as e:
            flash(str(e))
            return redirect(url_for('login.login'))
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    return render_template('login.html')

@login_bp.route('/logout')
def logout():
    session.pop('email_id', None)
    flash('You have been logged out.')
    return redirect(url_for('registration.index'))

@login_bp.route('/login')
def login():
    return render_template('login.html')




