from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from ..db import db
from ..models import Note
from ..schemas import NoteCreateSchema, NoteUpdateSchema, NoteSchema

blp = Blueprint(
    "Notes",
    "notes",
    url_prefix="/notes",
    description="Endpoints for creating, reading, updating, and deleting notes",
)

@blp.route("/")
class NotesList(MethodView):
    """Collection operations for notes."""

    # PUBLIC_INTERFACE
    @blp.response(200, NoteSchema(many=True), description="List all notes")
    @blp.doc(summary="List notes", description="Retrieve all notes ordered by most recently updated.")
    def get(self):
        """Return all notes ordered by updated_at desc."""
        notes = Note.query.order_by(Note.updated_at.desc()).all()
        return notes

    # PUBLIC_INTERFACE
    @blp.arguments(NoteCreateSchema)
    @blp.response(201, NoteSchema, description="Created note")
    @blp.doc(summary="Create note", description="Create a new note with title and content.")
    def post(self, data):
        """Create a new note."""
        note = Note(title=data["title"], content=data["content"])
        db.session.add(note)
        try:
            db.session.commit()
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            abort(400, message=f"Failed to create note: {str(e)}")
        return note


@blp.route("/<int:note_id>")
class NoteItem(MethodView):
    """Single note operations."""

    # PUBLIC_INTERFACE
    @blp.response(200, NoteSchema, description="A single note by ID")
    @blp.doc(summary="Get note", description="Get a note by its ID.")
    def get(self, note_id: int):
        """Get a note by id or 404."""
        note = Note.query.get(note_id)
        if not note:
            abort(404, message="Note not found")
        return note

    # PUBLIC_INTERFACE
    @blp.arguments(NoteUpdateSchema)
    @blp.response(200, NoteSchema, description="Updated note")
    @blp.doc(summary="Update note", description="Update fields of a note by its ID.")
    def patch(self, data, note_id: int):
        """Update a note partially by id."""
        note = Note.query.get(note_id)
        if not note:
            abort(404, message="Note not found")
        if "title" in data:
            note.title = data["title"]
        if "content" in data:
            note.content = data["content"]
        try:
            db.session.commit()
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            abort(400, message=f"Failed to update note: {str(e)}")
        return note

    # PUBLIC_INTERFACE
    @blp.response(204, description="Note deleted")
    @blp.doc(summary="Delete note", description="Delete a note by its ID.")
    def delete(self, note_id: int):
        """Delete a note by id."""
        note = Note.query.get(note_id)
        if not note:
            abort(404, message="Note not found")
        db.session.delete(note)
        try:
            db.session.commit()
        except (IntegrityError, SQLAlchemyError) as e:
            db.session.rollback()
            abort(400, message=f"Failed to delete note: {str(e)}")
        return ""
