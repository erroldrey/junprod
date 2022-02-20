from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Building


class BuildingModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


def create(self, validated_data):
    return Building(**validated_data)


def update(self, instance, validated_data):
    instance.geom = validated_data.get('geom', instance.geom)
    return instance


class BuildingSerializer(serializers.Serializer):
    geom = serializers.MultiPolygonField()


