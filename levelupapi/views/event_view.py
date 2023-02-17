"""View module for handling requests about event types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event
from levelupapi.models import Gamer, Game, gamer


class EventView(ViewSet):
    """Level up event view"""

    def retrieve(self, request, pk):
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)


    def list(self, request):
        [
    {
        "model": "levelupapi.game",
        "pk": 1,
        "fields": {
            "name": "Monopoly",
            "description": "Game that teaches you about capitalism",
            "genre": 1
        }
    },
    {
        "model": "levelupapi.game",
        "pk": 2,
        "fields": {
            "name": "Dungeons & Dragon",
            "description": "Dungeons & Dragons is a fantasy tabletop role-playing game originally designed by Gary Gygax and Dave Arneson.",
            "genre": 2
        }
    },
    {
        "model": "levelupapi.game",
        "pk": 3,
        "fields": {
            "name": "World of Warcraft",
            "description": "World of Warcraft is a massively multiplayer online role-playing game released in 2004 by Blizzard Entertainment.",
            "genre": 3
        }
    }
]
    def create(self, request):

        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        event = Event.objects.create(
            organizer=gamer,
            name=request.data["name"],
            date=request.data["date"],
            location=request.data["location"],
            game=game
            )
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all event
        Returns:
            Response -- JSON serialized list of event
        """
        # Make connection with server to retrieve a query set of all event items requested by client and assign the found instances to the event variable

        events = Event.objects.all()
        game = self.request.query_params.get('game')

        if game is not None:
            events = events.filter(game_id=game)
        else:
            pass
        # Set the `joined` property on every event
        for event in events:
            gamer = Gamer.objects.get(user=request.auth.user)
            # Check to see if the gamer is in the attendees list on the event
            event.joined = gamer in event.attendees.all()
        # passes instances stored in event variable to the serializer class to construct data into JSON stringified objects, which it then assigns to variable serializer
        serializer = EventSerializer(events, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event
    """
    class Meta:
        model = Event
        fields = ('id', 'organizer', 'name', 'date', 'location', 'game' )