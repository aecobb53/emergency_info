# Use the official Python image from the Docker Hub
FROM python

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY etc/requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY emergency_info emergency_info
COPY info.json info.json
COPY etc/entrypoint.sh .
