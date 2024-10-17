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

- Python 3.10 or higher
- Django 5.1.2 or higher
- Pip

* If on mac, you can either install Python via Python official website, https://www.python.org/downloads/release/python-3130/, or homebrew
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


## POSTMAN
You can download POSTMAN and use the collections and environment in the `postman` directory to make these calls.
To download POSTMAN: https://www.postman.com/downloads/

- Import the collection and environment
- Make sure to select the environment called `Upwork Test` to have the right `bearer_token` variables.

### Authentication
![auth](https://github.com/user-attachments/assets/0dcc78c6-0998-4a25-91cf-6d0f2cebf474)

The API uses JWT for authentication. To obtain a JWT token, send a POST request to the `/api/token/` endpoint with your username and password that you created from the `createsuperuser` command above:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
![token](https://github.com/user-attachments/assets/cf0ee101-b7d3-403c-a668-57a9a1dcb2e2)

The response will include an `access` token that you can use to authenticate requests to protected endpoints.

### API Endpoints

#### Time Slots

- **Create a Time Slot**:
  - **Endpoint**: `POST /api/timeslots/`
  - **Request Body**:
    ```json
    {
        "day_of_week": "3",
        "start_time": "02:00:00",
        "end_time": "03:00:00",
        "stop_time":"",
        "ids":[],
        "camera_ids": []
    }
    ```
    ![post](https://github.com/user-attachments/assets/76985e71-e1f4-49cb-b163-19eb88686ccd)


- **Read Time Slots**:
  - **Endpoint**: `GET /api/timeslots/`
  - **Description**: Retrieve a list of all time slots.
![get](https://github.com/user-attachments/assets/8491c975-7890-4666-be1a-4e091b568054)


- **Read a Specific Time Slot**:
  - **Endpoint**: `GET /api/timeslots/<id>/`
  - **Description**: Retrieve details of a specific time slot by ID.
 
![get2](https://github.com/user-attachments/assets/06b3b2f0-d24e-445a-b1d6-683057460625)


- **Update a Time Slot**:
  - **Endpoint**: `PUT /api/timeslots/<id>/`
  - **Request Body**:
    ```json
    {
        "day_of_week": "4",
        "start_time": "04:00:00",
        "end_time": "05:00:00",
        "stop_time": "",
        "ids": [],
        "camera_ids":[]
    }
    ```
    
![put](https://github.com/user-attachments/assets/f280362a-e6e2-487f-897d-29e8e61f78e7)


- **Delete a Time Slot**:
  - **Endpoint**: `DELETE /api/timeslots/<id>/`
  - **Description**: Delete a specific time slot by ID.
  - 

![delete](https://github.com/user-attachments/assets/ceda41f9-543b-4c41-b7dc-275f85b6e4d8)

## Conclusion

This is a fully functional API for managing a weekly schedule, complete with JWT authentication and Swagger UI documentation. Feel free to extend the application and customize it to meet your requirements.

For further questions , please refer to the project's GitHub repository.

## Additional Resources

- **Django Documentation**: [Django Docs](https://docs.djangoproject.com/en/stable/)
- **Django REST Framework Documentation**: [DRF Docs](https://www.django-rest-framework.org/)
- **djangorestframework-simplejwt Documentation**: [SimpleJWT Docs](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- **drf-spectacular Documentation**: [Spectacular Docs](https://drf-spectacular.readthedocs.io/en/latest/)


