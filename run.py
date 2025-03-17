import os
import sys
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)
print(BASE_DIR)
from expense_project import create_app


# Initialize the Flask application
os.environ['SECRET_KEY'] = 'alohsecretkey'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:almiviolad@localhost/trackxpense'
os.environ['JWT_SECRET_KEY'] = 'jwtexpensesecretkey'
app = create_app()



if __name__ == "__main__":
    # Run the application
    app.run(debug=True)  # Set debug=False in production
