import os
from app import app

if __name__ == "__main__":
    # Prefer BACKEND_PORT if set (commonly used by orchestrators), then PORT, then default 5000
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("BACKEND_PORT", os.getenv("PORT", "5000")))
    debug = bool(int(os.getenv("FLASK_DEBUG", "0")))

    # Emit a startup log to stdout for health/readiness debugging
    print(f"[notes_backend] Starting Flask app on {host}:{port} (debug={debug})", flush=True)
    app.run(host=host, port=port, debug=debug)
