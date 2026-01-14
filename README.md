# Frien Backend

Backend service for **Frien**, responsible for conversation storage, messaging, and API access.

Built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Alembic**. Designed to be modular, migration-safe, and easy to extend.

---

## Tech Stack

- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Uvicorn
- Docker (optional)

---

## Repository Structure

```
frien-be/
└── backend/
    ├── alembic/
    │   ├── versions/
    │   ├── env.py
    │   └── script.py.mako
    │
    ├── app/
    │   ├── api/
    │   │   ├── conversations.py
    │   │   ├── messages.py
    │   │   └── users.py
    │   │
    │   ├── core/
    │   │   └── config.py
    │   │
    │   ├── db/
    │   │   ├── base.py
    │   │   ├── engine.py
    │   │   ├── session.py
    │   │   ├── models.py
    │   │   └── schemas.py
    │   │
    │   ├── interaction/
    │   └── router.py
    │
    ├── .env
    ├── alembic.ini
    └── README.md
```

---

## Setup

### 1. Clone

```bash
git clone https://github.com/your-org/frien-be.git
cd frien-be/backend
```

---

### 2. Environment Variables

Create a `.env` file:

```env
```

---

### 3. Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### 4. Run the Server

```bash
uvicorn app.router:app --reload
```

Server runs at:
```
http://localhost:8000
```

---

## Database & Migrations

Generate a migration:
```bash
alembic revision --autogenerate -m "describe change"
```

Apply migrations:
```bash
alembic upgrade head
```

---

## API Overview

### Users
```
POST /users
GET  /users
```

### Conversations
```
POST /conversations
GET  /conversations/{id}
```

### Messages
```
POST /messages
GET  /messages?conversation_id=...
```

---

## Development Notes

- All DB access flows through `db/session.py`
- ORM models live in `db/models.py`
- Validation handled via Pydantic schemas
- API routes are split by domain
- Conversation logic lives in `interaction/`

---

## License

Private / MIT (update as needed)
