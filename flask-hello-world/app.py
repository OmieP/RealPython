# ---- Flask Hello World --- #

# Import the Flask class from the flask package
from flask import Flask

# Create the application object
app = Flask(__name__)

# Enable Debugging
app.config["DEBUG"] = True

# Use the decorator pattern to link the view function to a URL
@app.route("/")
@app.route("/hello")
# Define the view using a function, which returns a string
def hello_world():
    return "Hello, World!?!?!?!"

# Dynamic Route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name)
    else:
        return "Not Found", 404

# Start the development server using the run() method
if __name__ == "__main__":
    app.run()
