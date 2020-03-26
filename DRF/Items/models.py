import uuid 
from django.db import models

class Item(models.Model):
    uuid = models.UUIDField(primary_key=True)
    owner = models.UUIDField(null=True)
    type = models.UUIDField(null=True, default="null")
    actor_class = models.CharField(max_length=128, blank=False)
    location = models.CharField(max_length=64, blank=False)
    rotation = models.CharField(max_length=64, blank=False)
    owning_world_uuid = models.UUIDField()
    
    def __str__(self):
        return self.uuid.__str__()