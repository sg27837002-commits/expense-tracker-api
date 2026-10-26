# Expense Tracker API

A RESTful Expense Tracker API built with Django REST Framework. It allows users to create accounts, authenticate securely using JWT tokens, and manage their personal expenses.

## Features

- User registration
- JWT authentication
- Create, view, update, and delete expenses
- User-specific expense management
- Expense categories
- Filter expenses by week, month, or the last three months
- Filter expenses by a custom date range
- Django Admin integration
- Input validation through Django REST Framework serializers

## Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Postman
- Git and GitHub

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sg27837002-commits/expense-tracker-api.git
cd expense-tracker-api
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install django djangorestframework djangorestframework-simplejwt python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the project root and add:

```env
DJANGO_SECRET_KEY=replace-with-your-own-secret-key
```

Use a secure, randomly generated secret key. Never commit your real `.env` file to GitHub.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create an admin account

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

`http://127.0.0.1:8000/`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/signup/` | Register a user |
| POST | `/api/token/` | Obtain JWT tokens |
| POST | `/api/token/refresh/` | Refresh an access token |
| GET | `/api/expenses/` | List your expenses |
| POST | `/api/expenses/` | Create an expense |
| GET | `/api/expenses/<id>/` | Retrieve an expense |
| PATCH | `/api/expenses/<id>/` | Update an expense |
| PUT | `/api/expenses/<id>/` | Replace an expense |
| DELETE | `/api/expenses/<id>/` | Delete an expense |

## Authentication

Most expense endpoints require a valid JWT access token.

In Postman, select **Authorization → Bearer Token** and enter your access token.

### Example: Create an expense

Send a `POST` request to:

`http://127.0.0.1:8000/api/expenses/`

JSON body:

```json
{
  "title": "Grocery Shopping",
  "amount": "1500.00",
  "category": "Groceries",
  "description": "Weekly grocery items",
  "date": "2026-10-26"
}
```

The expense is automatically associated with the authenticated user.

## Expense Filters

### Weekly expenses

`GET /api/expenses/?period=week`

### Monthly expenses

`GET /api/expenses/?period=month`

### Last 90 days

`GET /api/expenses/?period=3months`

### Custom date range

`GET /api/expenses/?start_date=2026-10-01&end_date=2026-10-31`

## Available Categories

- Groceries
- Leisure
- Electronics
- Utilities
- Clothing
- Health
- Others

## Development Status

Core expense management, user registration, JWT authentication, and date filtering have been implemented and tested locally.

## Future Improvements

- Automated API tests
- Pagination
- Improved date-filter validation
- API documentation with Swagger or OpenAPI
- Deployment to a production hosting platform

## License

This project is currently intended for learning and portfolio development.
