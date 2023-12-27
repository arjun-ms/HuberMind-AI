# Use a base image with Python and your desired Linux distribution
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install any dependencies specified in requirements.txt
RUN pip install --upgrade -r requirements.txt

# Copy the entire project into the container
COPY . .
