# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . /app

# Install the application dependencies
RUN pip install -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production  # Set to production for deployment

# Expose port 5000 for Flask
EXPOSE 5000

# Define the entry point for the container, using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
