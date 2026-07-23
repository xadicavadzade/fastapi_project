# 🌿 Carpe Diem — Photo & Video Sharing Platform

A modern full-stack social media application built with **FastAPI**, **Streamlit**, **SQLAlchemy**, and **ImageKit**. The platform enables users to securely register, upload photos and videos, browse a live community feed, and manage their own posts through a clean and minimal interface.

---

## 🌍 Live Demo

### Backend API
> https://fastapi-project-66ph.onrender.com

### Frontend
> https://fastapi-project-1-wuqb.onrender.com

### API Documentation
> https://fastapi-project-66ph.onrender.com/docs

---

## 📸 Preview

<p align="center">
<img width="1917" alt="Login" src="https://github.com/user-attachments/assets/51727072-1fcd-4d13-8a63-d5000d2a3eb1">

<br><br>

<img width="1913" alt="Feed" src="https://github.com/user-attachments/assets/4ceea9be-ecab-4ad6-ab38-99555b9b78dc">

<br><br>

<img width="1917" alt="Upload" src="https://github.com/user-attachments/assets/d0b61195-24ce-4986-8259-eb2d06db7bfe">

<br><br>

<img width="1918" alt="Profile" src="https://github.com/user-attachments/assets/377f68ed-5db1-44fe-abfc-12a366796d80">
</p>

---

# 📖 Project Overview

Carpe Diem is a cloud-based media sharing application where users can create an account, upload photos and videos, browse posts shared by the community, and manage their own content.

The project demonstrates modern backend development using **FastAPI** together with a Python-based frontend built in **Streamlit**. Authentication is handled with JWT tokens, uploaded media is stored in **ImageKit**, and metadata is managed using **SQLAlchemy** with **SQLite**.

---

# 🏗️ System Architecture

```text
                    User
                      │
                      ▼
           Streamlit Frontend
               (Render)
                      │
                HTTP Requests
                      │
                      ▼
            FastAPI Backend
               (Render)
                      │
      ┌───────────────┴────────────────┐
      │                                │
      ▼                                ▼
 JWT Authentication              ImageKit Cloud
      │                                │
      ▼                                ▼
 SQLAlchemy ORM                  Images & Videos
      │
      ▼
    SQLite
```

---

# ✨ Features

- Secure JWT Authentication
- User Registration & Login
- Photo Upload
- Video Upload
- Optional Image Captions
- Cloud Media Storage
- ImageKit Transformations
- Community Feed
- Delete Own Posts
- Responsive Streamlit Interface
- Async FastAPI Backend
- Automatic OpenAPI Documentation
- RESTful API

---

# 🛠️ Technology Stack

## Backend

- FastAPI
- SQLAlchemy
- FastAPI Users
- SQLite
- Pydantic
- Uvicorn

## Frontend

- Streamlit
- Requests

## Cloud Services

- ImageKit

## Deployment

- Render
- Docker

---

# 📁 Project Structure

```text
FAST_API_
│
├── app/
│   ├── app.py
│   ├── db.py
│   ├── users.py
│   ├── schema.py
│   ├── images.py
│   └── __init__.py
│
├── frontend.py
├── main.py
├── requirements.txt
├── Dockerfile
├── .env
└── test.db
```

---

# 🚀 Running Locally

## Clone Repository

```bash
git clone https://github.com/your-username/your-repository.git

cd FAST_API_
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
IMAGEKIT_PUBLIC_KEY=YOUR_PUBLIC_KEY
IMAGEKIT_PRIVATE_KEY=YOUR_PRIVATE_KEY
IMAGEKIT_URL=YOUR_IMAGEKIT_URL
```

---

## Start Backend

```bash
python main.py
```

Backend:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

## Start Frontend

```bash
streamlit run frontend.py
```

Frontend:

```
http://localhost:8501
```

---

# 📡 REST API

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/register` | Register a new account |
| POST | `/auth/jwt/login` | Login and receive a JWT token |
| POST | `/auth/jwt/logout` | Logout |
| GET | `/users/me` | Get authenticated user |

---

## Posts

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload` | Upload an image or video |
| GET | `/feed` | Retrieve all posts |
| DELETE | `/posts/{id}` | Delete a post |

---

# 🗄️ Database

## User

- UUID Primary Key
- Email
- Password Hash
- One-to-Many relationship with Posts

---

## Post

| Field | Description |
|---------|-------------|
| id | UUID Primary Key |
| user_id | Post Owner |
| caption | Optional Caption |
| url | ImageKit Public URL |
| file_type | Image / Video |
| file_name | Stored Filename |
| created_at | Upload Timestamp |

---

# 🔒 Security

- JWT Authentication
- Protected API Endpoints
- Authorization Checks
- Environment Variables
- Secure Cloud Storage
- Owner-only Post Deletion

---

# ☁️ Deployment

## Backend

Hosted on **Render**

```
https://fastapi-project-1-wuqb.onrender.com
```

Swagger

```
https://fastapi-project-1-wuqb.onrender.com/docs
```

---

## Frontend

Hosted on **Render**

```
https://YOUR-FRONTEND.onrender.com
```

---

# 🚀 Future Improvements

- PostgreSQL
- User Profiles
- Likes & Comments
- Follow System
- Notifications
- Search
- Infinite Scrolling
- Docker Compose
- CI/CD Pipeline
- Unit & Integration Tests

---

# 💡 What This Project Demonstrates

This project highlights practical full-stack software engineering skills, including:

- FastAPI Application Development
- REST API Design
- JWT Authentication
- Async SQLAlchemy
- Database Modeling
- Cloud Media Storage with ImageKit
- Streamlit UI Development
- Docker Containerization
- Render Deployment
- Clean Project Architecture
- Python Backend Development

---

# 📄 License

This project was developed for educational and portfolio purposes.
