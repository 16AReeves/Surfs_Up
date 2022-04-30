# Import Dependencies
from flask import Flask

# Create a new Flask App Instance
app = Flask(__name__)


# Create a flask route
@app.route('/')
def hello_world():
    return 'Hello World! :)'
