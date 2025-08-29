import datetime as dt
from .db import db

class Note(db.Model):
    """Represents a note entity stored in the database."""
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, default="")
    content = db.Column(db.Text, nullable=False, default="")
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Note id={self.id} title={self.title!r}>"
