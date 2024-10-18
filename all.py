# Push Project to GitHub
git init 
git add .
git commit -m"initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main

# Configure PostgreSQL on Render and Connect Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Database configuration (use Render's URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://<user>:<password>@<host>/<database>'
app.config[SQLALCHEMY_DATABASE_MODIFICACTIONS] = False

db = SQLAlchemy(app)

# Add psycopg2 to your requirements.txt:
Flask
Flask-SQLAlchemy
psycopg2-binary
pytest
unittest

# 5. Implement Swagger Documentation in Flask
from flask import Flask
from flasgger import Swagger


app = Flask(__name__)

# Initialize Swagger
swagger = Swagger(app)

@app.route('/products', methods=['GET'])
def get_products():
    """
    Get All Products
    ---
    response:
      200:
        description: Returns a list of products
    """
    # Your logic to get products
    return {"products": []}

if __name__ == "__main__":
    app.run()

# 6. Running Tests
import unittest 
from app import app

class TestApp(unittest.TastCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_get_products(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertIn('products', response.json)

if __name__ == '__main__':
    unittest.main()


