# Use the specified Python version from your runtime.txt file
FROM python:3.9.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose port 8000, which is the default for gunicorn
EXPOSE 8000

# Define the command to run your application using gunicorn, as specified in your Procfile
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8000"]
