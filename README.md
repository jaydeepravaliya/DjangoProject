# DjangoProject - Login System

A Django-based **login system** with signup, login, profile management, and CRUD operations for user data.

## 📌 Features
- ✅ User Signup & Login
- ✅ Django Admin Panel for User Management
- ✅ CRUD Operations (Create, Read, Update, Delete Users)
- ✅ API Testing with **Postman**
---

## 🚀 Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/DjangoProject.git
cd DjangoProject
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser (Optional)
```bash
python manage.py createsuperuser
🔗 Visit Django Admin Panel: http://127.0.0.1:8000/admin/
```

### 6️⃣ Run the Server
```bash
python manage.py runserver
```


🔗 Open your browser and visit:

- **Signup Page** → [http://127.0.0.1:8000/signup/](http://127.0.0.1:8000/signup/)
- **Login Page** → [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

---

## 🛠 API Endpoints & Postman Collection

You can test all APIs using **Postman**.  
📂 **Postman Collection File:** [`Django_Login_System_Postman_Collection.json`](Django_Login_System_Postman_Collection.json)

### **Available Endpoints**

| Method  | Endpoint                     | Description                     |
|---------|------------------------------|---------------------------------|
| `POST`  | `/signup/`                   | Register a new user            |
| `POST`  | `/login/`                    | Authenticate user              |
| `GET`   | `/users/`                     | Retrieve all users             |
| `GET`   | `/users/<email>/`             | Get user details by email      |
| `POST`  | `/users/<email>/update/`      | Update user details            |
| `GET`   | `/users/<email>/delete/`      | Delete a user                  |

### 🔹 **How to Import Postman Collection:**
1. Open **Postman**.
2. Click **Import** → Select `Django_Login_System_Postman_Collection.json`.
3. Test all API endpoints.

