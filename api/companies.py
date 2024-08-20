from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from db_conn import db_connect

companies_bp = Blueprint('companies', __name__)

@companies_bp.route('/api/companies', methods=['GET'])
def get_companies():
    try:
        connection = db_connect()
        cursor = connection.cursor()
        companies = cursor.execute('SELECT company_name, company_details, location, experience, base_price, company_img FROM company')
        companies_data = cursor.fetchall() 
        company_list = [
            {
                "name": company[0],
                "details": company[1],
                "location": company[2],
                "experience": company[3],
                "price": company[4],
                "imgSrc": company[5]
            } for company in companies_data
        ]
        return jsonify(company_list)
    except Error as e:
            return jsonify({"message": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()