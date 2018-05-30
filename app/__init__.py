from flask import Flask
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.getcwd() + "/app/files_to_index"

from app import views
