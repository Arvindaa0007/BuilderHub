from flask import Flask, render_template, request, redirect, url_for, jsonify, Blueprint
from db_conn import db_connect
import os

post_company_bp = Blueprint('post_company', __name__)

#this function gets all companies from db
def get_companies_from_db():
    try:
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute("SELECT company_name, company_details, location, experience, base_price, img_src FROM company")
        companies = cursor.fetchall()   
    except Error as e:
        return jsonify({"message": str(e)}), 500
    finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    return [
        {
            'name': company[0],
            'details': company[1],
            'location': company[2],
            'experience': company[3],
            'price': company[4],
            'imgSrc': company[5]
        } for company in companies
    ]

@post_company_bp.route('/api/companies')
def companies():
    return jsonify(get_companies_from_db())

@post_company_bp.route('/')
def dashboard():
    return render_template('dashboard.html')

@post_company_bp.route('/post_company')
def post_company():
    return render_template('post_company.html')

@post_company_bp.route('/submit_company', methods=['POST'])
def submit_company():
    name = request.form['name']
    details = request.form['details']
    location = request.form['location']
    experience = request.form['experience']
    price = request.form['price']

    if 'imgsrc' in request.files:
        img_file = request.files['imgsrc']
        if img_file.filename != '':
            # img_path = os.path.join(app.config['UPLOAD_FOLDER'], img_file.filename)
            img_path = os.path.join('static/image', img_file.filename)
            img_file.save(img_path)

    try:
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO company (company_name, company_details, location, experience, base_price, img_src) VALUES (%s, %s, %s, %s, %s, %s)",
                    (name, details, location, experience, price, img_path))
        connection.commit()
    except Error as e:
        return jsonify({"message": str(e)}), 500
    finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()    
    return redirect(url_for('dashboard.dashboard'))


