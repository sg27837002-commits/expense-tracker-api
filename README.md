# Expense Tracker API

A RESTful Expense Tracker API built with Django REST Framework and JWT authentication. Users can register, securely log in, and manage their personal expenses.

## Features

- User registration
- JWT access and refresh token authentication
- Create, view, update, and delete expenses
- User-specific expense data protection
- Expense categories
- Filter expenses by week
- Filter expenses by month
- Filter expenses by the last 90 days
- Filter expenses using a custom date range
- Django Admin integration
- Input validation using Django REST Framework serializers

## Technology Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite
- Postman
- Git and GitHub

## Project Structure

```text
expense-tracker-api/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── expenses/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
├── .gitignore
├── README.md
└── manage.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sg27837002-commits/expense-tracker-api.git
cd expense-tracker-api
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process Bypass -Force
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install django djangorestframework djangorestframework-simplejwt python-dotenv
```

### 5. Configure environment variables

Create a `.env` file in the project root and add your own secret key:

```env
DJANGO_SECRET_KEY=replace-with-your-own-secret-key
```

Never upload your real `.env` file or production secret key to GitHub.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

The development server will run at:

http://127.0.0.1:8000/

Django Admin is available at:

http://127.0.0.1:8000/admin/

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/signup/` | Register a new user |
| POST | `/api/token/` | Obtain JWT tokens |
| POST | `/api/token/refresh/` | Refresh an access token |
| GET | `/api/expenses/` | List the authenticated user's expenses |
| POST | `/api/expenses/` | Create an expense |
| GET | `/api/expenses/<id>/` | Retrieve a specific expense |
| PUT | `/api/expenses/<id>/` | Replace an expense |
| PATCH | `/api/expenses/<id>/` | Partially update an expense |
| DELETE | `/api/expenses/<id>/` | Delete an expense |

## Authentication

Expense endpoints require a valid JWT access token.

To authenticate in Postman:

1. Send a `POST` request to `/api/token/`.
2. Provide your username and password as JSON.
3. Copy the returned access token.
4. Open the expense request's **Authorization** tab.
5. Select **Bearer Token** and enter the access token.

Do not share your access or refresh tokens publicly.

## Example: Register a User

**Request**

```http
POST /api/signup/
```

**JSON body**

```json
{
  "username": "exampleuser",
  "email": "example@example.com",
  "password": "Use-A-Strong-Password"
}
```

Use your own test details when testing locally.

## Example: Create an Expense

**Request**

```http
POST /api/expenses/
```

**JSON body**

```json
{
  "title": "Grocery Shopping",
  "amount": "1500.00",
  "category": "Groceries",
  "description": "Weekly grocery items",
  "date": "2026-10-26"
}
```

Send the request with a valid Bearer access token. The expense is associated with the authenticated user automatically.

## Expense Categories

- Groceries
- Leisure
- Electronics
- Utilities
- Clothing
- Health
- Others

## Expense Filters

### Weekly expenses

```http
GET /api/expenses/?period=week
```

### Monthly expenses

```http
GET /api/expenses/?period=month
```

### Last 90 days

```http
GET /api/expenses/?period=3months
```

### Custom date range

```http
GET /api/expenses/?start_date=2026-10-01&end_date=2026-10-31
```

You can use these query parameters to retrieve expenses matching the selected period or date range.

## Testing

The API has been tested locally using Postman for:

- User registration
- JWT token generation
- Listing expenses
- Creating expenses
- Updating expenses
- Deleting expenses
- Date-based filtering

## Security

- Environment variables are used for the Django secret key.
- `.env` is excluded through `.gitignore`.
- The local SQLite database and virtual environment are excluded from Git.
- Expense queries are restricted to the authenticated user.

For production deployment, configure a strong secret key, disable debug mode, configure allowed hosts, and use production-appropriate settings.

## Future Improvements

- Automated API tests
- Pagination
- Stronger date-filter validation
- API documentation with Swagger or OpenAPI
- Production deployment
- Continuous integration

## License

This project is currently intended for learning and portfolio development. A formal open-source license can be added later.
## Project Challenge

Built for the roadmap.sh Expense Tracker API project:
https://roadmap.sh/projects/expense-tracker-api
