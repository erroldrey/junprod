from math import radians, asin, sqrt, sin, cos

import django_filters.rest_framework
from django.contrib.auth.models import Building
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from JunBuildings.Buildapp.models import Building
from serializers import BuildingSerializer
from rest_framework import generics


class BuildingList(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('geom')

def get_distance_between_users(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    length = 2 * asin(sqrt(sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2))
    km = 6371 * length
    return round(km, 3)


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass
