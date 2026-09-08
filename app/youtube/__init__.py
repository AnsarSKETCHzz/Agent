import os
from flask import Flask, render_template
from youtube.routes import youtube_bp


def create_app():
    app = Flask(__name__)

    app.config["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

    app.register_blueprint(
        youtube_bp,
        url_prefix="/youtube"
    )

    @app.route("/")
    def home():
        return render_template("index.html")

    return app
