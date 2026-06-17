# 🌿 Carpe Diem — Photo & Video Sharing App

A full-stack media sharing application built with **FastAPI** (backend) and **Streamlit** (frontend), featuring JWT authentication, cloud image/video storage via **ImageKit**, and a clean, minimal UI.

---

## ✨ Features

- **User Authentication** — Register, login, and logout using JWT tokens (via `fastapi-users`)
- **Media Upload** — Share photos and videos with optional captions
- **Live Feed** — Browse all shared moments in reverse chronological order
- **ImageKit Integration** — Cloud-based media hosting with on-the-fly transformations (caption overlays, video resizing)
- **Delete Posts** — Owners can delete their own posts
- **Responsive UI** — Custom-styled Streamlit frontend with a teal aesthetic

---

## 🗂️ Project Structure

```
FAST_API_/
│
├── app/
│   ├── __init__.py
│   ├── app.py          # FastAPI routes (upload, feed, delete)
│   ├── db.py           # SQLAlchemy models & async database setup
│   ├── images.py       # ImageKit client initialization
│   ├── schema.py       # Pydantic schemas
│   └── users.py        # fastapi-users config (JWT auth)
│
├── frontend.py         # Streamlit frontend
├── main.py             # Uvicorn entry point
├── .env                # Environment variables (not committed)
├── .gitignore
└── test.db             # SQLite database (auto-created)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend API | [FastAPI](https://fastapi.tiangolo.com/) |
| Authentication | [fastapi-users](https://fastapi-users.github.io/) (JWT) |
| Database ORM | [SQLAlchemy](https://www.sqlalchemy.org/) (async) |
| Database | SQLite (via `aiosqlite`) |
| Media Storage | [ImageKit.io](https://imagekit.io/) |
| Frontend | [Streamlit](https://streamlit.io/) |
| Server | [Uvicorn](https://www.uvicorn.org/) |

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd FAST_API_
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy aiosqlite fastapi-users[sqlalchemy] imagekitio python-dotenv streamlit requests
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
IMAGEKIT_PUBLIC_KEY=your_public_key_here
IMAGEKIT_PRIVATE_KEY=your_private_key_here
IMAGEKIT_URL=https://ik.imagekit.io/your_imagekit_id
```

> You can find these values in your [ImageKit dashboard](https://imagekit.io/dashboard/developer/api-keys).

---

## 🚀 Running the Application

### Start the FastAPI backend

```bash
python main.py
```

The API will be available at `http://localhost:8000`.  
Interactive docs: `http://localhost:8000/docs`

### Start the Streamlit frontend

Open a second terminal (with the virtual environment activated):

```bash
streamlit run frontend.py
```

The frontend will open at `http://localhost:8501`.

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/jwt/login` | Login and receive a JWT token |
| `POST` | `/auth/jwt/logout` | Logout |
| `GET` | `/users/me` | Get current user info |

### Posts

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/upload` | Upload an image or video with a caption |
| `GET` | `/feed` | Get all posts (newest first) |
| `DELETE` | `/posts/{post_id}` | Delete a post (owner only) |

All post endpoints require a valid `Authorization: Bearer <token>` header.

---

## 🗄️ Database Models

### `User`
Extends `SQLAlchemyBaseUserTableUUID` from `fastapi-users`.  
Has a one-to-many relationship with `Post`.

### `Post`

| Field | Type | Description |
|---|---|---|
| `id` | UUID | Primary key |
| `user_id` | UUID | Foreign key to `User` |
| `caption` | Text | Optional post caption |
| `url` | String | Public ImageKit URL |
| `file_type` | String | `"image"` or `"video"` |
| `file_name` | String | Stored filename on ImageKit |
| `created_at` | DateTime | Upload timestamp |

---

## 🖼️ Frontend Pages

### Login / Register
- Email and password input
- **Login** button authenticates and stores the JWT in session state
- **Register** button creates a new account

### Feed (`🏠 Axın`)
- Displays all posts in reverse chronological order
- Images are rendered with an ImageKit caption overlay transformation
- Videos are rendered with padding/resize transformation
- Post owners see a **Delete** button

### Upload (`📎 Paylaş`)
- File uploader supporting PNG, JPG, MP4, AVI, MOV, MKV, WEBM
- Optional caption (max 300 characters)
- Uploads to ImageKit and saves metadata to the database

---

## 🔐 Security Notes

- JWT tokens are stored in Streamlit's `session_state` (client-side only)
- The `SECRET` key in `users.py` should be moved to the `.env` file before deploying to production
- The app currently uses SQLite; switch to PostgreSQL for production use

---

## 📝 License

This project was built for learning purposes. Feel free to use and extend it.