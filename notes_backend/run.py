import os
from app import app

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "5000"))
    debug = bool(int(os.getenv("FLASK_DEBUG", "0")))
    app.run(host=host, port=port, debug=debug)
