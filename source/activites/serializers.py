# serializers are done for each app

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import routers, serializers, viewsets, permissions
from .models import  Activity
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
class ActivitySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'event_name', 'event_location', 'event_description', 'event_image']

class ActivityViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializers


