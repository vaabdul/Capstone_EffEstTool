Estimation Tool:
----------------

Table of Contents
    Installation
    Usage
    Endpoints
    API Documentation
    
Installation
    Clone the repository.
    Install dependencies using pip install -r requirements.txt.
    Set up your MongoDB database and update the MONGO_URI in the Flask app configuration.
    Run the application using python app.py.

Usage
    Navigate to http://localhost:5000 in your web browser.
    Register a new user or log in with existing credentials.
    Access various endpoints for user management, estimation submission, and data manipulation.
    Explore the API endpoints or use them in your own applications.

Endpoints
    /register: POST endpoint for user registration.
    /login: POST endpoint for user login/authentication.
    /update/<string:id>: POST endpoint for updating user password.
    /delete/<string:id>: DELETE endpoint for deleting a user account.
    /logout: GET endpoint for user logout.
    /estimationform: POST endpoint for submitting estimation data.
    /estCalculate: POST endpoint for calculating project estimation based on historical data.   
    /tasks: PUT endpoint for updating the tasks

API Documentation
    Detailed API documentation and usage instructions can be found in the docstrings of the Flask application code.
    For API usage, refer to the API endpoints listed above.
