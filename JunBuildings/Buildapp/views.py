from math import radians, cos

from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Building
from .serializers import BuildingModelSerializer, BuildingSerializer


class BuildingModelViewSet(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingModelSerializer


class BuildingViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def get_queryset(self):
        try:
            distance = float(self.request.GET.get('distance'))
            mylon = self.request.user.profiles.longitude
            mylat = self.request.user.profiles.latitude
            lon1 = mylon - distance / abs(cos(radians(mylat)) * 111.0)
            lon2 = mylon + distance / abs(cos(radians(mylat)) * 111.0)
            lat1 = mylat - (distance / 111.0)
            lat2 = mylat + (distance / 111.0)
            queryset = Building.objects.filter(latitude__range=(lat1, lat2)).filter(longitude__range=(lon1, lon2))
            return queryset
        except TypeError:
            queryset = Building.objects.all()
            return queryset
