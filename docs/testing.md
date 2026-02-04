# Testing

## Backend smoke checks
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
In another terminal:
```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/api/v1/manufacturing/overview
curl http://127.0.0.1:8000/api/v1/mes/live
```

## Frontend smoke check
```bash
cd frontend
python -m http.server 5173
```
Open `http://localhost:5173` and verify the dashboard loads, theme toggle works, and the chart renders.

## Database schema validation
```bash
psql -d erp -f docs/database_schema.sql
```
