# Use the official Python image with a slim tag
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your Python application files into the container
COPY python_api.py .

# Install any necessary dependencies (example: Flask)
RUN pip install flask

# Expose the port your application will run on (e.g., Flask default is 5000)
EXPOSE 80
# PORT `80` will be exposed to be used by outside apps(like the browser in your local system )
# to interact with this app


# Set the FLASK_APP environment variable to specify the Flask application
ENV FLASK_APP=python_api

# Define the command to run your Python application
# CMD ["python", "python_api.py"] # command `python python_api.py` local machine but not in docker. Error 'Already in use'
CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]