From  python:latest

LABEL MAINTAINER="pd"

ADD . /VFGEO
WORKDIR /VFGEO

# Installing requirements
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt