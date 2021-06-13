# Get python image from docker hub
FROM python:3.9

# Change working directory inside the docker
WORKDIR /usr/src/app

# Copy all data from the host current directory to container WORKDIR
COPY . .

# Install all the required python packages/libraries using pip
RUN pip install -r requirements.txt

# Exposing port 8000 to the docker network so that
# we can connect with the docker container by publishing the port while running the same.
EXPOSE 8000

# Setting up the final command that should fire for running the conatiner
CMD uvicorn main:app --host=0.0.0.0
