# Get this image from Dockerhub
from python:3.6

# Copy the files to app directory
copy . /app

# Set the working directory to app
WORKDIR /app

# Install flask
RUN pip3.6 install flask requests

# Expose the ports
EXPOSE 5010

# Volume on host machine
#volume ["~/Desktop"]
 
# Run this command
CMD ["python3.6", "display.py"]
