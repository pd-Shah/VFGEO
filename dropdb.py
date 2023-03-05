import os
import django
from django.contrib.gis.geos import GEOSGeometry

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "VFGEO.settings")
django.setup()

import geopandas as gpd
from geo_api.models import Municipality


# Load GeoJSON file using geopandas
municipalities = gpd.read_file("dataset/dataset.geojson")

# Create Municipality objects and save them to the database
for index, row in municipalities.iterrows():

    geometry = GEOSGeometry(row["geometry"].wkt)

    municipality = Municipality(
        title=row["name"],
        geometry=geometry,
    )
    municipality.save()
