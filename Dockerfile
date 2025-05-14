# Use an official Python image as a base
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . .
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask application
EXPOSE 5000

# Run the main application script
CMD ["python", "main.py"]
