"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, Genre


class GameView(ViewSet):
    """Level up game view"""

    def retrieve(self, request, pk):
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)


    def list(self, request):
        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)

    def create(self, request):

        genre = Genre.objects.get(pk=request.data["genre"])

        game = Game.objects.create(
        name=request.data["name"],
        description=request.data["description"],
        genre=genre
    )
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        game = Game.objects.get(pk=pk)
        game.name = request.data["name"]
        game.description = request.data["description"]

        genre = Genre.objects.get(pk=request.data["genre"])
        game.genre = genre
        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        


class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game
    """
    class Meta:
        model = Game
        fields = ('id', 'name', 'description', 'genre' )
        depth= 1