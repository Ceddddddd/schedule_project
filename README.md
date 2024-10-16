
# Weekly Schedule API

This is a simple Django application that implements a CRUD API (Create, Read, Update, Delete) for managing a weekly schedule with IDs associated with time slots for each day of the week. The application includes Swagger documentation and uses JWT (JSON Web Token) for authentication.

## Features

- **CRUD Operations**: Create, read, update, and delete schedule entries.
- **JWT Authentication**: Secure the API using JWT tokens.
- **Swagger Documentation**: Automatically generated API documentation.

## Technologies Used

- Django
- Django REST Framework
- djangorestframework-simplejwt
- drf-spectacular

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Django 3.2 or higher
- Pip

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for accessing the Django admin)**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

### API Documentation

The API is documented using Swagger UI. To access the documentation, navigate to:

```
http://127.0.0.1:8000/swagger/
```

### Authentication

The API uses JWT for authentication. To obtain a JWT token, send a POST request to the `/api/token/` endpoint with your username and password:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

The response will include an `access` token that you can use to authenticate requests to protected endpoints.

### API Endpoints

#### Time Slots

- **Create a Time Slot**:
  - **Endpoint**: `POST /api/timeslots/`
  - **Request Body**:
    ```json
    {
        "day_of_week": "Monday",
        "start_time": "09:00:00",
        "end_time": "17:00:00"
    }
    ```

- **Read Time Slots**:
  - **Endpoint**: `GET /api/timeslots/`
  - **Description**: Retrieve a list of all time slots.

- **Read a Specific Time Slot**:
  - **Endpoint**: `GET /api/timeslots/<id>/`
  - **Description**: Retrieve details of a specific time slot by ID.

- **Update a Time Slot**:
  - **Endpoint**: `PUT /api/timeslots/<id>/`
  - **Request Body**:
    ```json
    {
        "day_of_week": "Monday",
        "start_time": "10:00:00",
        "end_time": "18:00:00"
    }
    ```

- **Delete a Time Slot**:
  - **Endpoint**: `DELETE /api/timeslots/<id>/`
  - **Description**: Delete a specific time slot by ID.

## Conclusion

This is a fully functional API for managing a weekly schedule, complete with JWT authentication and Swagger UI documentation. Feel free to extend the application and customize it to meet your requirements.

For further questions , please refer to the project's GitHub repository.

## Additional Resources

- **Django Documentation**: [Django Docs](https://docs.djangoproject.com/en/stable/)
- **Django REST Framework Documentation**: [DRF Docs](https://www.django-rest-framework.org/)
- **djangorestframework-simplejwt Documentation**: [SimpleJWT Docs](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- **drf-spectacular Documentation**: [Spectacular Docs](https://drf-spectacular.readthedocs.io/en/latest/)
