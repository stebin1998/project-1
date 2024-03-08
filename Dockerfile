# Utilizing Python 3.11 slim as the foundation
FROM python:3.11-slim

# Establishing the directory within the container for all operations
WORKDIR /code

# Transferring the entire project's files into the container
COPY . /code

# Making the app's port available to the host
EXPOSE 8010

# Initiating the Python server to output the current time in Toronto via a JSON response for GET requests
CMD ["python", "./server.py"]

# Instructions to build the Docker image:
# Execute the command: docker build -t stebingeorge/healthcare-service:v1 .
# To launch the container, use:
# Execute the command: docker run -p 8010:8010 stebingeorge/healthcare-service:v1
