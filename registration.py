from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from db_conn import db_connect
from werkzeug.security import generate_password_hash

registration_bp = Blueprint('registration', __name__)

# this is main index function
@registration_bp.route('/')
def index():
    return render_template('Registration.html')

@registration_bp.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.json
        connection = None
        cursor = None

        try:
            connection = db_connect()
            cursor = connection.cursor()

            hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

            add_user = (
                "INSERT INTO User (companyName, companyTelephone, first_name, middle_name, last_name, mobile_number, email_id, password, state, city, street1, street2, pin_code, sex, Age, DOB) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            )

            user_data = (
                data.get('companyName'), data.get('companyTelephone'), data['firstName'], data.get('middleName'), data['lastName'],
                data['mobileNumber'], data['emailId'], hashed_password, data['state'], data['city'], data['street1'],
                data.get('street2'), data['pinCode'], data['sex'], data['age'], data['dob']
            )

            cursor.execute(add_user, user_data)
            connection.commit()

            # return jsonify(message="User successfully created!")
            return jsonify({"message": "User successfully created!", "redirect_url": url_for('login.login')})
        except Error as e:
            return jsonify({"message": str(e)}), 500
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    else:
        return render_template('Registration.html')