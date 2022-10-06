FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt /app

# Install any dependencies
RUN pip install -r requirements.txt

### Start Appdynamics ###
RUN pip install --upgrade pip
RUN pip install -U appdynamics
COPY appdynamics.cfg /app
### End Appdynamics ###

# Copy the content of the local src directory to the working directory
COPY src /app

# By default, listen on port 8081
EXPOSE 8081/tcp
ENV FLASK_PORT=8081

# Specify the command to run on container start
CMD [ "python", "./app.py" ]

#RUN pyagent -c appdynamics.conf << command >>