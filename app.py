from flask import Flask
from flask_cors import CORS
from login import login_bp  
from registration import registration_bp  
from dashboard import dashboard_bp
from post_company import post_company_bp
from api.companies import companies_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = 'static/image'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

app.register_blueprint(login_bp)
app.register_blueprint(registration_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(post_company_bp)
app.register_blueprint(companies_bp)

if __name__ == '__main__':
    app.run(debug=True)





