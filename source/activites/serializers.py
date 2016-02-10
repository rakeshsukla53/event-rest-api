# serializers are done for each app

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from .models import  Activity

class ActivitySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'event_name', 'event_location', 'event_description', 'event_image']

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers


