# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app code and requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Expose port and start the app
EXPOSE 5000
CMD ["python", "app.py"]
