# User Registration API

## Description

This is a simple User Registration API built with Django and Django Rest Framework (DRF). It allows users to register with a set of required information such as `username`, `email`, `password`, `first_name`, and `last_name`.

## Project Setup
### Requirements
- Python 3.9.6
- Django
- Django Rest Framework

### Installation
1. Install Python.
2. Install Django and Django Rest Framework:
   ```
   pip install django djangorestframework
   ```
3. Clone or download the repository:
   ```
   git clone <repository_link>
   ```
4. Navigate to the project directory:
   ```
   cd <project_folder>
   ```
5. Migrate the database:
   ```
   python manage.py migrate
   ```
6. Run the server:
   ```
   python manage.py runserver
   ```

## Usage
The API endpoint for user registration is available at `/api/register/`.

Send a `POST` request to that URL with the following data format:
   ```
   {
       "username": "Username",
       "password1": "Password",
       "password2": "Password", (should match with password1)
       "email": "user@example.com",
       "first_name": "First Name",
       "last_name": "Last Name"
   }
   ```
If the registration is successful, the created user object details (without password) will be returned as a response.

## License
This project is licensed under the terms of the MIT license.

## Contact
Any further questions, feedback, or suggestions, please direct them to the [GitHub Issues](https://github.com/username/projectname/issues) section of this project.
   ```

Please replace the `<repository_link>`, `<project_folder>`, `username` and `projectname`, with the actual values.