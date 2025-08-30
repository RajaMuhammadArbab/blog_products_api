
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
## PROJECT_DEMO ##
## 1 ##
<img width="1435" height="610" alt="4" src="https://github.com/user-attachments/assets/4613e7d8-2e83-45f8-a878-a198b54d8c76" />
## 2 ##
<img width="1462" height="888" alt="5" src="https://github.com/user-attachments/assets/9daf6ddf-60ee-4680-9326-1acf820955fe" />
## 3 ##
<img width="1435" height="877" alt="6" src="https://github.com/user-attachments/assets/7f0cabe5-8b2a-4ca8-a281-c935e3d552fd" />
## 4 ##
<img width="1437" height="893" alt="8" src="https://github.com/user-attachments/assets/d5968a5f-32e1-47be-93d4-c9e18276946b" />
## 5 ##
<img width="1432" height="893" alt="7" src="https://github.com/user-attachments/assets/39bb9145-5dd1-4ad7-9347-6020e63a367e" />
## 6 ##
<img width="1373" height="781" alt="10" src="https://github.com/user-attachments/assets/b42008db-f187-4d3f-9830-830bc3f2204d" />
## 7 ##
<img width="1370" height="785" alt="18" src="https://github.com/user-attachments/assets/f146b5b2-4336-4176-91e0-d4bf70e38881" />
## 8 ##
<img width="1388" height="884" alt="15" src="https://github.com/user-attachments/assets/28952667-e5c2-479c-b5a8-9f940eb4b034" />
## 9 ##
<img width="1382" height="899" alt="16" src="https://github.com/user-attachments/assets/8a921cf4-8294-44de-aaa9-696ee3ef9660" />
## 10 ##
<img width="1378" height="885" alt="17" src="https://github.com/user-attachments/assets/3f53d456-e802-4ed9-9e77-85bbcede8e6d" />
## 11 ##
<img width="1366" height="456" alt="14" src="https://github.com/user-attachments/assets/4f4bed18-3820-41c8-bd65-9cb605db01db" />

