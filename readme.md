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
    /update_password: POST endpoint for updating user password.
    /delete_user: DELETE endpoint for deleting a user account.
    /logout: GET endpoint for user logout.
    /estimation_submission: POST endpoint for submitting estimation data.
    /display_details: POST endpoint for displaying historical data on selecting application type.
    /estimation_calculation: POST endpoint for calculating project estimation based on historical data.
    /historical_data: GET endpoint for displaying historical estimation data.
    /his_delete_item/<string:id>: DELETE endpoint for deleting a historical estimation data item.
    /his_update_item/<string:id>: POST endpoint for updating a historical estimation data item.
    /update_task_form: PUT endpoint for updating the estimated data.

API Documentation
    Detailed API documentation and usage instructions can be found in the docstrings of the Flask application code.
    For API usage, refer to the API endpoints listed above.