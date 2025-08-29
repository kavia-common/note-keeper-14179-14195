# note-keeper-14179-14195

Backend: Flask Notes API

- Install dependencies:
  pip install -r notes_backend/requirements.txt

- Configure environment:
  cp notes_backend/.env.example notes_backend/.env
  # Optionally adjust DATABASE_URL, PORT, etc.

- Run:
  cd notes_backend
  python run.py

- API Docs:
  Visit http://localhost:5000/docs to explore OpenAPI docs.

Endpoints:
- GET /           -> Health
- GET /notes/     -> List notes
- POST /notes/    -> Create note
- GET /notes/{id} -> Get single note
- PATCH /notes/{id} -> Update note
- DELETE /notes/{id} -> Delete note