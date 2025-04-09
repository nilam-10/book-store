# 📚 Django Bookstore App

A fully functional, user-authenticated online bookstore built with Django and Bootstrap. Users can sign up, log in, browse a curated list of books, add/remove them from a shopping cart, and view their selections with a total price summary.

---

## 🚀 Features

- 👤 User Authentication (Signup, Login, Logout)
- 📘 Browse a catalog of books with title, author, and price
- 🛒 Add/remove books from a shopping cart
- 💵 Dynamic cart summary with total price
- 🎨 Clean, responsive UI powered by Bootstrap 5

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/bookstore.git
cd bookstore
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
```

#### Activate the Environment

- **Windows**  
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**  
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Now visit 👉 http://127.0.0.1:8000

---

## 🔐 Create Admin User (Optional)

To access the Django Admin Panel:

```bash
python manage.py createsuperuser
```

Visit 👉 http://127.0.0.1:8000/admin

---

## 📓 Sample Book Data (Preloaded)

| Title               | Author              | Price |
|--------------------|---------------------|-------|
| The Alchemist       | Paulo Coelho        | ₹399  |
| Atomic Habits       | James Clear         | ₹499  |
| Python Crash Course | Eric Matthes        | ₹650  |
| Deep Work           | Cal Newport         | ₹450  |
| 1984                | George Orwell       | ₹350  |
| Sapiens             | Yuval Noah Harari   | ₹550  |
| Rich Dad Poor Dad   | Robert Kiyosaki     | ₹299  |
| Clean Code          | Robert C. Martin    | ₹799  |
| Zero to One         | Peter Thiel         | ₹399  |
| The Lean Startup    | Eric Ries           | ₹499  |

---






