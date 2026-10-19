import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Development server. For real hosting use:  waitress-serve --listen=0.0.0.0:8000 run:app
    app.run(host=os.environ.get("VR_HOST", "127.0.0.1"), port=int(os.environ.get("VR_PORT", "5000")), debug=os.environ.get("VR_DEBUG", "0") == "1")
