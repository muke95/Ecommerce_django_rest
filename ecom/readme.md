# Django E-commerce API

This is a basic Django API project with authentication, product fetching, and cart management functionality.

## 📂 Project Structure

project_name/
├── ecomapp/
│ ├── views.py # Contains API view functions
│ ├── urls.py # API route definitions
│ ├── models.py # Database models
│ ├── serializers.py # Data serialization
├── ecom/
│ ├── settings.py # Project configuration
│ ├── urls.py # Main URL configuration
└── manage.py # Django project manager



---

## 📌 API Endpoints

| Method | Endpoint      | Description |
|--------|--------------|-------------|
| GET    | `/`           | Test response from the API |
| GET    | `/product/`   | Fetch all product details |
| POST   | `/signup/`    | Create a new user account |
| POST   | `/login/`     | Log in a user and create a session |
| POST   | `/logout/`    | Log out the user |
| GET/POST | `/cart/`   | View or add items to the cart |

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/muke95/Ecommerce_django_rest.git
   cd ecom


2. **Create and activate a virtual environment**

    bash
    Copy
    Edit
    python -m venv venv
    source venv/bin/activate      # On macOS/Linux
    venv\Scripts\activate         # On Windows

3.  **Install dependencies**
    pip install -r requirements.txt

4.  **Apply migrations**
    python manage.py makemigrations
    python manage.py migrate

5.  **Create a superuser (for Django admin access)**
    python manage.py createsuperuser

6.  **Run the development server**
    python manage.py runserver
7.  **Access the API**
    API Root: http://127.0.0.1:8000/

    Admin Panel: http://127.0.0.1:8000/admin/




