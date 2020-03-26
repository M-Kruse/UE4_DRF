from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Items.models import Item
from .models import Heartbeat

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['uuid', 'owning_world_uuid', 'owner', 'type', 'location', 'rotation']

class HeartbeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Heartbeat
        fields = ['healthy']

