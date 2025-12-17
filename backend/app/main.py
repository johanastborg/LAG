from flask import Flask
from flask_cors import CORS
from app.api.routes import main_bp
import os

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register Blueprints
    app.register_blueprint(main_bp, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
