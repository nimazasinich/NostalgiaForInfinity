<<<<<<< HEAD
# Use the official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install virtualenv
RUN pip install virtualenv

# Create a virtual environment
RUN virtualenv venv

# Activate the virtual environment and upgrade pip
RUN . venv/bin/activate && pip install --upgrade pip

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies in the virtual environment
RUN . venv/bin/activate && pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the entrypoint to activate the virtual environment and run the app
ENTRYPOINT ["/bin/bash", "-c", ". venv/bin/activate && exec python main.py"]
=======
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Nostalgia For Infinity API!"

@app.route("/api/data", methods=["GET"])
def get_data():
    data = {
        "message": "Hello, world!",
        "status": "success"
    }
    return jsonify(data)

@app.route("/api/data", methods=["POST"])
def post_data():
    data = request.json
    return jsonify({"received": data, "status": "success"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> cdac0ecc (Save local changes before rebase)
