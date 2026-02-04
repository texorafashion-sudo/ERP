# Installation

## Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Frontend (static preview)
```bash
cd frontend
python -m http.server 5173
```
Open `http://localhost:5173` in a browser.

## Database
1. Create a PostgreSQL database named `erp`.
2. Apply the schema:
```bash
psql -d erp -f docs/database_schema.sql
```
3. Seed the sample data (optional):
```bash
python -m app.seed.sample_data
```

## Environment
Update `backend/app/core/config.py` with production secrets and connection strings.

## Testing
See `docs/testing.md` for smoke-test and health-check commands.
