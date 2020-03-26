from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Players.models import Player
#from Inventory.models import Item


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['player_id', 'create_date']
