# FastAPI + SQLModel CRUD API

This project is a simple **CRUD REST API** built with **FastAPI** and
**SQLModel**, using **SQLAlchemy** for database interaction and
**PostgreSQL / SQLite / any SQL database** via environment
configuration. It demonstrates clean project structure, dependency
injection, and database lifecycle management.

------------------------------------------------------------------------

## 🚀 Features

-   FastAPI-based REST API
-   SQLModel ORM (built on SQLAlchemy + Pydantic)
-   Automatic database table creation
-   Dependency-injected DB sessions
-   Environment-based configuration using `.env`
-   Full CRUD operations:
    -   Create item
    -   Read all items
    -   Read item by ID
    -   Update item
    -   Delete item

------------------------------------------------------------------------

## 🛠 Tech Stack

-   **Python 3.10+**
-   **FastAPI**
-   **SQLModel**
-   **SQLAlchemy**
-   **Uvicorn**
-   **python-dotenv**

------------------------------------------------------------------------

## 📂 Project Structure

    .
    ├── main.py
    ├── .env
    └── README.md

------------------------------------------------------------------------

## ⚙️ Setup & Installation

### 1. Clone the repository

``` bash
git clone <your-repo-url>
cd <your-project>
```

### 2. Create a virtual environment

``` bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

``` bash
pip install fastapi uvicorn sqlmodel python-dotenv
```

------------------------------------------------------------------------

## 🗄 Database Configuration

Create a `.env` file in the project root:

``` env
DATABASE_URL=sqlite:///./database.db
```

Or for PostgreSQL:

``` env
DATABASE_URL=postgresql+psycopg2://user:password@localhost/dbname
```

------------------------------------------------------------------------

## ▶️ Running the Application

``` bash
uvicorn main:app --reload
```

Server will start at:

    http://127.0.0.1:8000

------------------------------------------------------------------------

## 📘 Interactive API Docs

-   Swagger UI: http://127.0.0.1:8000/docs\
-   ReDoc: http://127.0.0.1:8000/redoc

------------------------------------------------------------------------

## 📌 API Endpoints

### ➕ Create Item

POST `/items/`

``` json
{
  "name": "Laptop",
  "description": "Lenovo ThinkPad"
}
```

### 📄 Get All Items

GET `/items`

### 🔍 Get Item by ID

GET `/items/{item_id}`

### ✏️ Update Item

PATCH `/items/{item_id}`

``` json
{
  "name": "Updated Name"
}
```

### ❌ Delete Item

DELETE `/items/{item_id}`

------------------------------------------------------------------------

## 🧠 Implementation Details

-   Uses FastAPI lifespan events to:
    -   Test DB connection at startup
    -   Automatically create database tables
    -   Properly close DB connections on shutdown
-   Database sessions are injected via `Depends()`
-   Uses SQLModel for ORM + schema validation

------------------------------------------------------------------------

## 🧑‍💻 Author

Built as a learning and demonstration project using **FastAPI +
SQLModel**.
