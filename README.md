# GeoJSON CRUD REST API with Django and DRF

This project is a CRUD REST API for GeoJSON feature objects. It allows users to create, read, update, and delete GeoJSON features through a REST API.
Technologies Used

```bash
Python 3
Django
Django REST framework
PostGIS
GeoPandas
GDAL
```

## Setup Instructions

## install Docker on Ubuntu:

Update the package index:

```bash

sudo apt-get update
sudo apt-get install docker-ce
```

Verify that Docker is installed correctly by running the hello-world image:

```bash
sudo docker run hello-world
```

If Docker is installed correctly, you should see a message that says “Hello from Docker!” followed by some additional information.

## Clone the repository:

```bash
git clone https://github.com/pd-Shah/VFGEO
```

## Running

To run the project using Docker Compose, follow these steps:

```bash
sudo docker-compose up --build
```

The command will start the PostgreSQL and the Django server. Once the server is running, you should be able to access the API at http://localhost:8000/.

## Authentication

This project uses JSON Web Tokens (JWTs) for authentication.
