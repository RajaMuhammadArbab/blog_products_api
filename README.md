
# 📖 Blog & Products API  

This API allows managing blog posts, products, categories, tags, and users. It supports CRUD operations, search, filtering, and ordering.  

---

## 🚀 Setup Instructions
```bash
# clone repo
git clone <your-repo-url>
cd project

# install dependencies
pip install -r requirements.txt

# migrate database
python manage.py migrate

# create superuser (optional)
python manage.py createsuperuser

# run server
python manage.py runserver
```

---

## 🔑 Authentication
- Register user: `POST /api/users/`  
- Login: `POST /api/token/` (if JWT enabled)  

---

## 📌 Endpoints

### Users
```http
POST /api/users/ 
{
  "username": "john",
  "email": "john@example.com",
  "password": "1234"
}
```

### Categories
```http
POST /api/categories/
{
  "name": "Technology"
}
```

### Tags
```http
POST /api/tags/
{
  "name": "Django"
}
```

### Blog Posts
```http
POST /api/blogs/
{
  "title": "My First Blog",
  "content": "This is a sample blog.",
  "author": 1,
  "category_id": 1,
  "tag_ids": [1]
}
```

### Products
```http
POST /api/products/
{
  "title": "Laptop",
  "description": "Gaming Laptop",
  "category_id": 1,
  "tag_ids": [1],
  "price": 1200.50,
  "available": true
}
```

---

## 🔍 Search, Filter & Ordering Examples

### 🔎 Blog Search
```http
GET /api/blogs/?search=First
```
**Response**
```json
{
  "count": 1,
  "results": [
    {
      "id": 1,
      "title": "My First Blog",
      "content": "This is a sample blog.",
      "author": 1,
      "category": {"id": 1, "name": "Technology"},
      "tags": [{"id": 1, "name": "Django"}],
      "published_date": "2025-08-30T10:00:00Z"
    }
  ]
}
```

### 🏷️ Filter by Category
```http
GET /api/blogs/?category_id=1
```

### 🏷️ Filter by Tag
```http
GET /api/blogs/?tags__id=1
```

### ⏳ Ordering
```http
GET /api/blogs/?ordering=-published_date
```

### 🔎 Product Search
```http
GET /api/products/?search=Laptop
```

### 💰 Product Price Range
```http
GET /api/products/?price_min=500&price_max=1500
```

---

## 📸 Example Screenshots / JSON  

📝 Blog list response:
```json
{
  "count": 2,
  "results": [
    {
      "id": 1,
      "title": "My First Blog",
      "content": "This is a sample blog.",
      "author": 1,
      "category": {"id": 1, "name": "Technology"},
      "tags": [{"id": 1, "name": "Django"}],
      "published_date": "2025-08-30T10:00:00Z"
    }
  ]
}
```

🛒 Product list response:
```json
{
  "count": 1,
  "results": [
    {
      "id": 1,
      "title": "Laptop",
      "description": "Gaming Laptop",
      "category": {"id": 1, "name": "Technology"},
      "tags": [{"id": 1, "name": "Django"}],
      "price": "1200.50",
      "available": true
    }
  ]
}
```
