# Jewelry Backend API

A RESTful backend service for managing jewelry products and categories. Built with Django REST Framework and JWT authentication, this API provides secure user authentication and complete product management functionality for an e-commerce jewelry platform.

## Features

### Authentication

* User Registration
* User Login
* JWT Access & Refresh Tokens
* Protected API Endpoints

### Product Management

* Create Products
* Retrieve Products
* Update Products
* Delete Products
* Search Products
* Filter Products by Price and Metal Type
* Sort Products by Price

### Category Management

* List Categories
* Retrieve Products by Category

---

## Tech Stack

| Technology            | Purpose                      |
| --------------------- | ---------------------------- |
| Python                | Backend Programming Language |
| Django                | Web Framework                |
| Django REST Framework | REST API Development         |
| Simple JWT            | Authentication               |
| SQLite                | Database                     |
| Django CORS Headers   | Cross-Origin Requests        |

---

## Project Structure

```text
Jewelry_backend/
│
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── auth_views.py
│   ├── urls.py
│   └── admin.py
│
├── jewelry_backend/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## Database Models

### Category

| Field     | Type    |
| --------- | ------- |
| id        | Integer |
| name      | String  |
| image_url | URL     |

### Product

| Field       | Type        |
| ----------- | ----------- |
| id          | Integer     |
| name        | String      |
| description | Text        |
| category    | Foreign Key |
| price       | Decimal     |
| discount    | Decimal     |
| base_metal  | String      |
| polish      | String      |
| rating      | Float       |
| image_url   | URL         |

---

## API Endpoints

### Authentication

#### Register User

```http
POST /api/users/register/
```

Request Body:

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "password123"
}
```

---

#### Login User

```http
POST /api/users/login/
```

Request Body:

```json
{
  "username": "john",
  "password": "password123"
}
```

Response:

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

---

## Products API

### Get All Products

```http
GET /api/products/
```

### Get Product By ID

```http
GET /api/products/{id}/
```

### Create Product

```http
POST /api/products/add/
```

### Update Product

```http
PUT /api/products/{id}/update/
```

### Delete Product

```http
DELETE /api/products/{id}/delete/
```

---

## Categories API

### Get All Categories

```http
GET /api/categories/
```

### Get Products By Category

```http
GET /api/categories/{id}/products/
```

---

## Filtering & Search

### Filter By Minimum Price

```http
GET /api/products/?min_price=500
```

### Filter By Maximum Price

```http
GET /api/products/?max_price=5000
```

### Filter By Metal Type

```http
GET /api/products/?metal=Gold
```

### Sort Products By Price

```http
GET /api/products/?sort=price
```

### Search Products

```http
GET /api/products/?search=ring
```

---

## Authentication Flow

```text
Register User
      │
      ▼
Login User
      │
      ▼
Receive JWT Token
      │
      ▼
Send Token in Header
      │
      ▼
Access Protected APIs
```

Authorization Header:

```http
Authorization: Bearer <access_token>
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Lokeshreddy04/Jewelry_backend.git
cd Jewelry_backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run Development Server

```bash
python manage.py runserver
```

API will be available at:

```text
http://127.0.0.1:8000/
```

---

## Example Request

```bash
curl -X GET http://127.0.0.1:8000/api/products/
```

---

## Future Enhancements

* Swagger/OpenAPI Documentation
* PostgreSQL Integration
* Product Image Uploads
* Pagination
* Wishlist Functionality
* Shopping Cart APIs
* Order Management
* Role-Based Access Control
* Deployment on Render or AWS

---

## Screenshots

Create a `screenshots/` folder and add screenshots of:

* User Registration
* User Login
* Products API
* Categories API
* Postman Testing

Example:

```text
screenshots/
├── login.png
├── register.png
├── products.png
└── categories.png
```

---

## Author

**Lokesh Reddy**

GitHub: https://github.com/Lokeshreddy04

---

## License

This project is licensed under the MIT License.
