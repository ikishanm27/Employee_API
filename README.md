# Employees API

A RESTful API built with FastAPI for managing employee records and user authentication. This project features JWT-based authentication, role-based access control, and PostgreSQL database integration.

## Features

- **Authentication**: Secure user registration and login using JWT (JSON Web Tokens).
- **Role-Based Access Control (RBAC)**: 
  - **Admin**: Can manage all employee records and view users.
  - **User**: Basic access (default role).
- **Employee Management**: 
  - Create, Read, Update, and Delete (CRUD) operations.
  - Pagination support for listing employees.
  - Filtering by department and role.
- **Database**: Robust data persistence using PostgreSQL and SQLAlchemy ORM.

## Tech Stack

- **Language**: Python
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Security**: OAuth2, PyJWT (python-jose), Passlib (bcrypt)

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository_url>
   ```

2. **Install Dependencies**
   Ensure you have Python installed. It is recommended to use a virtual environment.
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose[cryptography] passlib[bcrypt]
   ```

3. **Database Configuration**
   - Ensure PostgreSQL is running locally on port `5432`.
   - Create a database named `postgres`.
   - Update the database connection string in `app/db.py` if your credentials differ from the default:
     ```python
     db_url="postgresql://postgres:1234@localhost:5432/postgres"
     ```

4. **Run the Server**
   Navigate to the project root and run:
   ```bash
   uvicorn main:app --reload
   ```
   *(Note: Ensure you have a `main.py` that initializes the FastAPI app and includes the routers)*

## Running Tests

This project uses `pytest` for testing. The tests are located in the `tests/` directory and use an in-memory SQLite database to ensure test isolation and speed, without affecting the development database.

1. **Install testing dependencies:**
   ```bash
   pip install pytest httpx
   ```

2. **Run the tests:**
   From the project root directory, run:
   ```bash
   pytest -v
   ```

## API Endpoints

### Authentication (`/user`)

- **POST** `/user/register`: Register a new user account.
- **POST** `/user/login`: Login to obtain an access token.
- **GET** `/user/all`: Retrieve a list of all registered users (Admin only).

### Employees (`/api`)

- **POST** `/api/employees`: Create a new employee record.
- **GET** `/api/employees`: List employees.
  - Query Params: `page`, `limit`, `department`, `role`.
- **GET** `/api/employee`: Get a single employee by ID.
  - Query Param: `id`.
- **PUT** `/api/employee`: Update an employee record.
  - Query Param: `id`.
- **DELETE** `/api/employee`: Delete an employee record.
  - Query Param: `id`.

Access the interactive API docs at `http://127.0.0.1:8000/docs` when the server is running.
