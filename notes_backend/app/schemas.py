from marshmallow import Schema, fields, validate

class NoteCreateSchema(Schema):
    """Schema for creating a new note."""
    title = fields.String(required=True, validate=validate.Length(min=1, max=255), metadata={"description": "Title of the note"})
    content = fields.String(required=True, metadata={"description": "Content of the note"})

class NoteUpdateSchema(Schema):
    """Schema for updating an existing note."""
    title = fields.String(required=False, validate=validate.Length(min=1, max=255))
    content = fields.String(required=False)

class NoteSchema(Schema):
    """Schema for serializing a note."""
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    content = fields.String(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
