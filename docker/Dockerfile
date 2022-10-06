FROM quay.io/devfile/python:slim

# By default, listen on port 8081
EXPOSE 8081/tcp
ENV FLASK_PORT=8081

# Set the working directory in the container
WORKDIR /projects

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

### Start Appdynamics ###
CMD pip install --upgrade pip
CMD pip install -U appdynamics
#COPY appdynamics.cfg /opt/appdynamics/appdynamics.cfg
### End Appdynamics ###

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "python", "./app.py" ]

#RUN pyagent -c appdynamics.conf << command >>