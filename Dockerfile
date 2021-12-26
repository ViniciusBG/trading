# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copying only requirements
COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .