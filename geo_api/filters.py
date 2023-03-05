from django_filters import rest_framework as filters
from django.contrib.gis.geos import Polygon
from .models import Municipality


class MunicipalityFilter(filters.FilterSet):
    bbox = filters.CharFilter(method="filter_bbox")

    def filter_bbox(self, queryset, name, value):
        bbox = value.split(",")
        min_x, min_y, max_x, max_y = map(float, bbox)
        polygon = Polygon.from_bbox((min_x, min_y, max_x, max_y))
        return queryset.filter(geometry__intersects=polygon)

    class Meta:
        model = Municipality
        fields = ["bbox"]
