# 📚 Shelves

A REST API allowing users to manage their personal book collections.

# **Features**
- *User Authentication:* Users can register, login and logout
- *Book Management:* Users can add, remove, and update books in their collection
- *Bookshelf Management:* Users can add, remove, and update bookshelves
- *Search & Filter:* Users can search and filter books and bookshelves

## **Installation**

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/kweku-xvi/shelves>

2. **Change directory:**
   ```bash
    cd shelves

3. **Create a virtual environment:**
   ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate  # For Windows

4. **Install dependencies:**
   ```bash
    pip install -r requirements.txt

5. **Apply migrations:**
   ```bash
    python manage.py makemigrations
    python manage.py migrate

6. **Create super user:**
   ```bash
    python manage.py createsuperuser

7. **Run development server:**
   ```bash
    python manage.py runserver

Open your server at [http://localhost:8000](http://localhost:8000)
