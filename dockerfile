# Use the official Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install virtualenv
RUN pip install virtualenv
<<<<<<< HEAD

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
ENTRYPOINT ["/bin/bash", "-c", ". venv/bin/activate && exec python <your_main_script>.py"]
=======

# Create and activate a virtual environment
RUN virtualenv venv
SHELL ["/bin/bash", "-c"]
RUN source venv/bin/activate && pip install --upgrade pip

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies in the virtual environment
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the entrypoint to activate the virtual environment and run the app
ENTRYPOINT ["bash", "-c", "source venv/bin/activate && exec python main.py"]
>>>>>>> cdac0ecc (Save local changes before rebase)
