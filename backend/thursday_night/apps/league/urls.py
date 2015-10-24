from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

from thursday_night.apps.league.models import Player, Event, Session, Result


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name')


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'start_date', 'end_date')


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'event', 'date')


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'session', 'player', 'points')


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'events', EventViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'results', ResultViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
]