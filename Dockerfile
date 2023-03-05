FROM thinkwhere/gdal-python:latest

LABEL MAINTAINER="pd"

ADD . /VFGEO
WORKDIR /VFGEO

# Installing requirements
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt