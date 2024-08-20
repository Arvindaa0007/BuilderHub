from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from db_conn import db_connect
from werkzeug.security import check_password_hash

dashboard_bp = Blueprint('dashboard', __name__)
login_bp = Blueprint('login', __name__)
registration_bp = Blueprint('Registration', __name__)
post_company_bp = Blueprint('post_company', __name__)

db_config = {
    'user': 'root',
    'password': 'password@123',
    'host': 'localhost',
    'database': 'build'
}

@dashboard_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@login_bp.route('/process_login', methods=['GET', 'POST'])
def process_login():
    return render_template('login.html')

@registration_bp.route('/registration', methods=['GET', 'POST'])
def register():
    return render_template('Registration.html')

@post_company_bp.route('/post_company', methods=['GET', 'POST'])
def register():
    return render_template('post_company.html')