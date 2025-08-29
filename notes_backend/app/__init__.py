import os
from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.url_map.strict_slashes = False

# CORS configuration - allow all origins by default
CORS(app, resources={r"/*": {"origins": os.getenv("CORS_ORIGINS", "*")}})

# OpenAPI / Swagger UI configuration
app.config["API_TITLE"] = os.getenv("API_TITLE", "Notes Backend API")
app.config["API_VERSION"] = os.getenv("API_VERSION", "v1")
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = os.getenv("OPENAPI_URL_PREFIX", "/docs")
app.config["OPENAPI_SWAGGER_UI_PATH"] = ""
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Database configuration defaults to SQLite
# Use DATABASE_URL env var to override (e.g., postgres://, mysql+pymysql://, etc.)
default_sqlite_path = os.path.join(os.getcwd(), "notes.db")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", f"sqlite:///{default_sqlite_path}")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create API and register blueprints
api = Api(app)

# Initialize database
from .db import db  # noqa: E402
db.init_app(app)

# Ensure tables exist on startup
with app.app_context():
    db.create_all()

# Import and register blueprints
from .routes.health import blp as health_blp  # noqa: E402
from .routes.notes import blp as notes_blp  # noqa: E402

api.register_blueprint(health_blp)
api.register_blueprint(notes_blp)
