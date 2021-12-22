"""
__init__.py tells the world this is a package AND
gets the nest made at startup
"""
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# from app import routes - default if user names appDir "app" - BOO HISS
# correct line is inserted during generation 'from appDir import routes'
from Fred import routes