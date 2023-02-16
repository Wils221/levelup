"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Genre


class GenreView(ViewSet):
    """Level up genre view"""

    def retrieve(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)


    def list(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)


class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for genre
    """
    class Meta:
        model = Genre
        fields = ('id', 'genre')
