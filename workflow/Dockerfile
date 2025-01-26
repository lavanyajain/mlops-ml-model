# Start with a different base image
FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Upgrade pip
RUN pip install --upgrade pip

# Adding requirements and installing Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
