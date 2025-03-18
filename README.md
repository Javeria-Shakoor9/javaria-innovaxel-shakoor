# 🚀 URL Shortener API

## 📌 Project Overview
This is a **Django REST Framework-based URL Shortener API** that allows users to:
- **Create** a short URL from a long URL.
- **Retrieve** the original URL using the short URL.
- **Update** an existing short URL.
- **Delete** a short URL.
- **Get statistics** on a short URL (e.g., number of times accessed).

## 📂 Repository Structure
- `main` branch → Contains only the `README.md`.
- `dev` branch → Contains the full project source code.

---

## ⚡ Tech Stack
- **Backend:** Python, Django REST Framework (DRF)
- **Database:** MySQL
- **Version Control:** Git & GitHub
- **API Documentation:** Postman

---

## 🛠️ Installation & Setup
### 🔹 1. Clone the Repository

git clone https://github.com/Javeria-Shakoor9/javaria-innovaxel-shakoor.git
cd javaria-innovaxel-shakoor


### 🔹 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 🔹 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 4. Configure MySQL Database
1. Open MySQL and create a database:
   ```sql
   CREATE DATABASE url_shortener_db;
   ```
2. Update `settings.py` with your MySQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'url_shortener_db',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

### 🔹 5. Apply Migrations & Run the Server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🔗 API Endpoints
--------------------------------------------------------------------------------
| HTTP Method | Endpoint                           | Description               |
|-------------|------------------------------------|---------------------------|
| **POST**    | `/api/shorten/`                    | Create a new short URL    |
| **GET**     | `/api/shorten/<short_code>/`       | Retrieve the original URL |
| **PUT**     | `/api/shorten/<short_code>/`       | Update a short URL        |
| **DELETE**  | `/api/shorten/<short_code>/`       | Delete a short URL        |
| **GET**     | `/api/shorten/<short_code>/stats/` | Get short URL statistics  |

### 📌 Example API Requests
#### **1. Create a Short URL (POST)**
```json
{
  "url": "https://www.example.com/long-url"
}
```
#### **2. Retrieve an Original URL (GET)**
```json
{
  "id": "1",
  "url": "https://www.example.com/long-url",
  "shortCode": "abc123",
  "createdAt": "2021-09-01T12:00:00Z",
  "updatedAt": "2021-09-01T12:00:00Z"
}
```
#### **3. Get URL Stats (GET)**
```json
{
  "id": "1",
  "url": "https://www.example.com/long-url",
  "shortCode": "abc123",
  "accessCount": 10
}
```

---

## 👥 Contributors
- **Javaria Shakoor**

---

## 📩 Contact
For any queries, feel free to reach out:
📧 Email: javeriashakoor9@gmail.com

