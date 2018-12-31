from rest_framework.serializers import BaseSerializer
from rest_framework import serializers

class MoviesSerializer(serializers.Serializer):
    name = serializers.CharField()
    date = serializers.CharField()
    location = serializers.CharField()
    directors = serializers.CharField()


